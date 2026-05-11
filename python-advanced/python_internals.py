"""
Python Internals: GIL, Threading vs Multiprocessing, and Garbage Collection

This file demonstrates:
- The Global Interpreter Lock (GIL) and how it affects CPU-bound tasks
- Threading versus multiprocessing for CPU/I/O-bound workloads
- Memory management and garbage collection
"""

import concurrent.futures
import gc
import os
import time


def cpu_bound_task(n):
    """A CPU-bound loop that computes a sum."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def io_bound_task(seconds):
    """Simulate I/O-bound work with sleep."""
    time.sleep(seconds)
    return seconds


def run_threading(target, args_list):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(target, args_list))
    duration = time.time() - start
    return duration, results


def run_multiprocessing(target, args_list):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(target, args_list))
    duration = time.time() - start
    return duration, results


def demonstrate_gil():
    print("=== GIL and concurrency demonstration ===")
    values = [5000000] * 4
    cpu_time_thread, _ = run_threading(cpu_bound_task, values)
    cpu_time_process, _ = run_multiprocessing(cpu_bound_task, values)
    print(f"CPU-bound with threads: {cpu_time_thread:.2f}s")
    print(f"CPU-bound with processes: {cpu_time_process:.2f}s")
    print(
        "Note: In CPython, the GIL limits true parallelism for CPU-bound threads,"
        " so multiprocessing is often faster for this kind of work."
    )
    print()

    sleep_times = [1] * 4
    io_time_thread, _ = run_threading(io_bound_task, sleep_times)
    io_time_process, _ = run_multiprocessing(io_bound_task, sleep_times)
    print(f"I/O-bound with threads: {io_time_thread:.2f}s")
    print(f"I/O-bound with processes: {io_time_process:.2f}s")
    print(
        "I/O-bound tasks often benefit from threading because the GIL is released"
        " during blocking operations like sleep."
    )


def demonstrate_garbage_collection():
    print("\n=== Garbage Collection and Memory Management ===")
    print("Current GC thresholds:", gc.get_threshold())
    print("Collecting garbage manually...")
    collected = gc.collect()
    print(f"Unreachable objects collected: {collected}")
    print("Creating objects and deleting references...")

    class Node:
        def __init__(self):
            self.reference = None

    a = Node()
    b = Node()
    a.reference = b
    b.reference = a
    print("Created cyclic reference between objects")

    del a
    del b
    collected = gc.collect()
    print(f"Garbage collected after removing references: {collected}")
    print("Reference counting plus cyclic GC help reclaim memory in Python.")


def main():
    print("Python Internals Demonstration")
    print("Process ID:", os.getpid())
    print("=" * 30)
    demonstrate_gil()
    demonstrate_garbage_collection()


if __name__ == "__main__":
    main()