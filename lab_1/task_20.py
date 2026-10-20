#!/usr/bin/env python3

def dive_in(l):
    if isinstance(l, list):
        for t in l:
            yield from dive_in(t)
    else:
        yield l

def unique_elements(l):
    result = []
    seen = set()
    for x in dive_in(l):
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def main():
    list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
    list_b = unique_elements(list_a)
    print(list_b)

if __name__ == "__main__":
    main()
