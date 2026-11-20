#!/usr/bin/env python3

import functools

def type_check(*types):
    def internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(types) != len(args):
                raise TypeError("недопустимое количество аргументов")
            if kwargs:
                raise TypeError("именованные аргументы не поддерживаются")
            if not all(map(lambda x: isinstance(x[0], x[1]), zip(args, types))):
                raise TypeError("недопустимый тип аргумента")
            return func(*args, **kwargs)
        return wrapper
    return internal

@type_check(int, int)
def my_sum_int(a, b):
    return a+b

@type_check(float, float)
def my_sum_float(a, b):
    return a+b

def main():
    print("my_sum_int(11, 20) = "+str(my_sum_int(11, 20)))
    print("11 + 20 можно для my_sum_int")
    try:
        print("my_sum_int(11, 20.) = "+str(my_sum_int(11, 20.)))
    except TypeError:
        print("11 + 20. не можно для my_sum_int")
    try:
        print("my_sum_int(11., 20.) = "+str(my_sum_int(11., 20.)))
    except TypeError:
        print("11. + 20. не можно для my_sum_int")
    print("my_sum_float(11., 20.) = "+str(my_sum_float(11., 20.)))
    print("11. + 20. можно для my_sum_float")
    try:
        print("my_sum_float(11, 20.) = "+str(my_sum_float(11, 20.)))
    except TypeError:
        print("11 + 20. не можно для my_sum_float")

if __name__ == "__main__":
    main()
