#!/usr/bin/env python3

import functools

from task_21 import factorial, timing

def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal cache_dict
        k = (args, tuple(kwargs.items()))
        if k in cache_dict:
            return cache_dict[k]
        result = func(*args, **kwargs)
        cache_dict[k] = result
        return result
    return wrapper

factorial_cached = timing(cache(factorial))

def main():
    factorial_cached(90000)
    factorial_cached(70000)
    factorial_cached(70000)
    factorial_cached(90000)

if __name__ == "__main__":
    main()
