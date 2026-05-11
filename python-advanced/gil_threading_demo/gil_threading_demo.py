"""
GIL, Threading, and Multiprocessing Demo

This module shows:
- The Global Interpreter Lock (GIL) effect on CPU-bound tasks
- Threading vs multiprocessing for CPU-bound and I/O-bound workloads
"""

import concurrent.futures
import time


def cpu_bound(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


def io_bound(seconds):
    time.sleep(seconds)
    return seconds


def measure(task, args_list, executor_cls):
    start = time.perf_counter()
    with executor_cls() as executor:
        results = list(executor.map(task, args_list))
    elapsed = time.perf_counter() - start
    return elapsed, results


def main():
    print("GIL, Threading, and Multiprocessing Demo")
    print("=" * 40)

    cpu_args = [2000000] * 4
    thread_time, _ = measure(cpu_bound, cpu_args, concurrent.futures.ThreadPoolExecutor)
    process_time, _ = measure(cpu_bound, cpu_args, concurrent.futures.ProcessPoolExecutor)

    print(f"CPU-bound with threads: {thread_time:.2f}s")
    print(f"CPU-bound with processes: {process_time:.2f}s")
    print("In CPython, the GIL prevents threads from executing Python bytecode in parallel for CPU-heavy work.")
    print("Multiprocessing can bypass the GIL by using separate interpreter processes.")

    io_args = [1] * 4
    thread_time, _ = measure(io_bound, io_args, concurrent.futures.ThreadPoolExecutor)
    process_time, _ = measure(io_bound, io_args, concurrent.futures.ProcessPoolExecutor)

    print(f"I/O-bound with threads: {thread_time:.2f}s")
    print(f"I/O-bound with processes: {process_time:.2f}s")
    print("I/O-bound operations often benefit from threads because the GIL is released during blocking I/O.")


if __name__ == "__main__":
    main()