#!/usr/bin/env python3

from task_5 import num

def main():
    set_1 = set(num(x) for x in input("Введите первый набор: ").split())
    set_2 = set(num(x) for x in input("Введите второй набор: ").split())

    print("1. Числа, которые есть в обоих наборах: ", set_1&set_2)
    print("2.1. Числа из первого набора, которые отсутствуют во втором", set_1-set_2)
    print("2.2. Числа из второго набора, которые отсутствуют в первом", set_2-set_1)
    print("3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1", set_1^set_2)

if __name__ == "__main__":
    main()
