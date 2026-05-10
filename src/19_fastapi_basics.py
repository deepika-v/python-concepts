"""
FastAPI Basics: Building a Simple REST API

FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

This example demonstrates:
- Creating a FastAPI application
- Defining API endpoints with HTTP methods
- Using Pydantic models for request/response validation
- Path parameters and query parameters
- Running the server with Uvicorn

To run this example:
1. Install dependencies: pip install fastapi uvicorn
2. Run: uvicorn 19_fastapi_basics:app --reload
3. Open http://127.0.0.1:8000/docs for interactive API documentation
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI(
    title="Python Concepts - FastAPI Demo",
    description="A simple API demonstrating FastAPI features",
    version="1.0.0"
)

# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    tax: Optional[float] = None

# In-memory storage (in production, use a database)
items_db = [
    Item(id=1, name="Laptop", price=999.99, description="A powerful laptop", tax=99.99),
    Item(id=2, name="Mouse", price=29.99, description="Wireless mouse", tax=3.00)
]

# Root endpoint
@app.get("/")
async def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to FastAPI Basics Demo"}

# Get all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    """Retrieve all items."""
    return items_db

# Get item by ID (path parameter)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """Retrieve a specific item by ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create new item (POST request)
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Create a new item."""
    # Check if item ID already exists
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")

    items_db.append(item)
    return item

# Update item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    """Update an existing item."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"Item {deleted_item.name} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Query parameter example
@app.get("/items/search/")
async def search_items(name: Optional[str] = None, min_price: Optional[float] = None):
    """Search items by name and/or minimum price."""
    results = items_db

    if name:
        results = [item for item in results if name.lower() in item.name.lower()]

    if min_price is not None:
        results = [item for item in results if item.price >= min_price]

    return {"results": results, "count": len(results)}

# Example of dependency injection (simple authentication simulation)
def get_current_user():
    """Simulate getting current user (in real app, this would check tokens)."""
    return {"username": "demo_user", "role": "admin"}

@app.get("/protected/")
async def protected_endpoint(current_user: dict = Depends(get_current_user)):
    """Protected endpoint requiring authentication."""
    return {"message": f"Hello {current_user['username']}! This is a protected endpoint."}

# Run the server (only if this file is run directly)
if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    print("Open http://127.0.0.1:8000/docs for API documentation")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)