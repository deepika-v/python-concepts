"""
Context Manager Examples

This file demonstrates:
- Custom context managers using __enter__ and __exit__
- Generator-based context managers with contextlib
- Safe resource handling patterns
"""

import contextlib
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")
        return False


class FileWriter:
    def __init__(self, path, mode="w"):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False


@contextlib.contextmanager
def managed_connection(name):
    print(f"Opening connection: {name}")
    try:
        yield {"connection": name}
    finally:
        print(f"Closing connection: {name}")


def main():
    print("Context Managers Demonstration")
    print("=" * 30)

    with Timer() as timer:
        total = sum(i * i for i in range(100000))
        print("Computed total:", total)

    with FileWriter("context_demo.txt", "w") as writer:
        writer.write("Context manager demo\n")

    with managed_connection("database") as conn:
        print("Working with", conn)

    print("Context managers help guarantee cleanup and error safety.")


if __name__ == "__main__":
    main()