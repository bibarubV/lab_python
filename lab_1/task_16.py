#!/usr/bin/env python3

from task_20 import dive_in

def flatten_list(l):
    return list(dive_in(l))

def main():
    list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
    list_b = flatten_list(list_a)
    print(list_b)

if __name__ == "__main__":
    main()
