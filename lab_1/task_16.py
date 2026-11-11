#!/usr/bin/env python3

def flatten_list(l):
    i = 0
    while i < len(l):
        if isinstance(l[i], list):
            flatten_list(l[i])
            t = l.pop(i)
            for j in range(len(t)-1, -1, -1):
                l.insert(i, t[j])
        else:
            i += 1

def main():
    list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
    flatten_list(list_a)
    print(list_a)

if __name__ == "__main__":
    main()
