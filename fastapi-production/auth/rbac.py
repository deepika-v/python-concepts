"""
Role-Based Access Control (RBAC)

This module provides:
- Role checking dependencies for FastAPI
- Hierarchical role permissions
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from fastapi_production.auth.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class RoleChecker:
    """Dependency for checking user roles."""

    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    async def __call__(self, token: str = Depends(oauth2_scheme)):
        try:
            payload = verify_token(token)
            user_role = payload.get("role")
            if user_role not in self.allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions"
                )
            return payload
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )

# Predefined role checkers
admin_only = RoleChecker(["admin"])
user_or_admin = RoleChecker(["user", "admin"])
moderator_or_admin = RoleChecker(["moderator", "admin"])