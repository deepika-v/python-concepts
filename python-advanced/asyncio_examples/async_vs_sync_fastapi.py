"""
Async Programming Examples and FastAPI Comparison

This file demonstrates:
- asyncio, async/await, and the event loop
- Async I/O concurrency patterns
- Comparing synchronous and asynchronous FastAPI endpoints
"""

import asyncio
import time

from fastapi import FastAPI


app = FastAPI(
    title="Python Concepts - Async vs Sync FastAPI",
    version="1.0.0",
    description="Demonstrates async and sync endpoints with asyncio concepts."
)


async def async_task(delay):
    await asyncio.sleep(delay)
    return f"async after {delay}s"


def sync_task(delay):
    time.sleep(delay)
    return f"sync after {delay}s"


async def demonstrate_asyncio():
    print("=== asyncio Demonstration ===")
    start = time.perf_counter()
    results = await asyncio.gather(async_task(1), async_task(1), async_task(1))
    elapsed = time.perf_counter() - start
    print("Async results:", results)
    print(f"Total async elapsed: {elapsed:.2f}s")

    start = time.perf_counter()
    results = [sync_task(1) for _ in range(3)]
    elapsed = time.perf_counter() - start
    print("Sync results:", results)
    print(f"Total sync elapsed: {elapsed:.2f}s")
    print(
        "Async allows the event loop to run other awaitable tasks while waiting for I/O-like operations."
    )


@app.get("/sync")
def read_sync():
    return {"status": sync_task(1), "type": "sync"}


@app.get("/async")
async def read_async():
    return {"status": await async_task(1), "type": "async"}


def main():
    print("Async Programming Demonstration")
    print("=" * 30)
    asyncio.run(demonstrate_asyncio())
    print("Run this file with uvicorn to compare FastAPI endpoints:")
    print("uvicorn python-advanced.asyncio_examples.async_vs_sync_fastapi:app --reload")


if __name__ == "__main__":
    main()