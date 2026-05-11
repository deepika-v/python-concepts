"""
Production-Ready FastAPI Application

This application demonstrates:
- OAuth2 + JWT authentication
- Role-based access control (RBAC)
- Middleware (logging, correlation ID, rate limiting)
- Observability (Prometheus metrics, structured logging)
- Async database integration (SQLAlchemy + MongoDB)
- Comprehensive testing with pytest

Run with: uvicorn fastapi_production.main:app --reload
"""

import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import List, Optional

import structlog
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from prometheus_client import Counter, Histogram, generate_latest
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fastapi_production.auth.jwt import create_access_token, verify_token
from fastapi_production.auth.rbac import RoleChecker
from fastapi_production.middleware.logging import LoggingMiddleware
from fastapi_production.middleware.rate_limiting import RateLimitMiddleware
from fastapi_production.observability.metrics import setup_metrics
from fastapi_production.observability.structured_logging import setup_structured_logging

# Setup structured logging
setup_structured_logging()
logger = structlog.get_logger()

# Database configurations
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
MONGODB_URL = "mongodb://localhost:27017"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# SQLAlchemy setup
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    role: Mapped[str] = mapped_column(default="user")
    is_active: Mapped[bool] = mapped_column(default=True)

# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None

# Role checkers
admin_only = RoleChecker(["admin"])
user_or_admin = RoleChecker(["user", "admin"])

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting FastAPI production application")
    app.state.sql_engine = create_async_engine(DATABASE_URL, echo=True)
    app.state.mongo_client = AsyncIOMotorClient(MONGODB_URL)
    app.state.mongo_db = app.state.mongo_client["fastapi_prod"]

    # Create tables
    async with app.state.sql_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    # Shutdown
    logger.info("Shutting down FastAPI production application")
    await app.state.sql_engine.dispose()
    app.state.mongo_client.close()

# FastAPI app
app = FastAPI(
    title="FastAPI Production Demo",
    description="Production-ready FastAPI with auth, middleware, observability, and async DB",
    version="1.0.0",
    lifespan=lifespan
)

# Add middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup metrics
setup_metrics(app)

# Dependency to get DB session
async def get_db():
    async with AsyncSession(app.state.sql_engine) as session:
        yield session

# Auth functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_user(db: AsyncSession, username: str):
    result = await db.execute(
        db.query(User).filter(User.username == username)
    )
    return result.scalars().first()

async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, role=payload.get("role"))
    except Exception:
        raise credentials_exception

    user = await get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if user exists
    db_user = await get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.get("/users/me/", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/users/", response_model=List[UserResponse])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(user_or_admin),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        db.query(User).offset(skip).limit(limit)
    )
    users = result.scalars().all()
    return users

@app.get("/admin/users/", response_model=List[UserResponse])
async def read_all_users(
    current_user: User = Depends(admin_only),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(db.query(User))
    users = result.scalars().all()
    return users

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    return generate_latest()

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# MongoDB example endpoint
@app.post("/items/")
async def create_item(item: dict):
    """Create an item in MongoDB."""
    result = await app.state.mongo_db.items.insert_one(item)
    return {"id": str(result.inserted_id), **item}

@app.get("/items/")
async def read_items():
    """Read items from MongoDB."""
    items = []
    async for item in app.state.mongo_db.items.find():
        items.append(item)
    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)