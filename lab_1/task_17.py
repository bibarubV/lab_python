#!/usr/bin/env python3

def merge_dicts(dict_a, dict_b):
    for k in dict_b:
        if k in dict_a:
            if isinstance(dict_a[k], dict) and isinstance(dict_b[k], dict):
                merge_dicts(dict_a[k], dict_b[k])
            else:
                dict_a[k] = dict_b[k]
        else:
            dict_a[k] = dict_b[k]

def main():
    dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
    dict_b = {"d": 1, "b": {"c": 2, "e": 3}} 
    merge_dicts(dict_a, dict_b)
    print(dict_a)

if __name__ == "__main__":
    main()
