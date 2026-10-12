#!/usr/bin/env python3

import functools
import time

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Затрачено времени (мс): "+str((end-start)*1000))
        return result
    return wrapper

@timing
def test():
    time.sleep(1)

@timing
def test2():
    def factorial(n):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
    factorial(90000)

def main():
    test()
    test2()

if __name__ == "__main__":
    main()
