#!/usr/bin/env python3

import functools
from datetime import datetime

def log_calls(fn):
    def internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            f = open(fn, "a", encoding="utf-8-sig")
            f.write(f"{datetime.now()}: function '{func.__name__}' called with positional arguments {args} and keyword arguments {kwargs}\n")
            f.close()
            return func(*args, **kwargs)
        return wrapper
    return internal

@log_calls("task_18.log")
def logged_print(*args, **kwargs):
    print(*args, **kwargs)

def main():
    logged_print("привет")
    logged_print("test")
    logged_print(1, 2, 3, sep="")

if __name__ == "__main__":
    main()
