#!/usr/bin/env python3

from task_5 import num

def main():
    nums = [num(x) for x in input("Введите ряд чисел: ").split()]

    unique = set()
    repeating = set()
    even = set()
    odd = set()
    negative = set()
    floats = set()
    sum_5 = 0
    largest = nums[0]
    smallest = nums[0]

    for n in nums:
        if n in unique:
            unique.remove(n)
            repeating.add(n)
        else:
            unique.add(n)
            if isinstance(n, float):
                floats.add(n)
            else:
                if n % 2 == 0:
                    even.add(n)
                else:
                    odd.add(n)
            if n < 0:
                negative.add(n)
            largest = max(largest, n)
            smallest = min(smallest, n)
        if isinstance(n, int) and n % 5 == 0:
            sum_5 += n

    print("Уникальные числа:", unique)
    print("Повторяющиеся числа:", repeating)
    print("Четные числа:", even)
    print("Нечетные числа:", odd)
    print("Отрицательные числа:", negative)
    print("Числа с плавающей точкой", floats)
    print("Сумма чисел, кратных 5:", sum_5)
    print("Наибольшее число:", largest)
    print("Наименьшее число:", smallest)

if __name__ == "__main__":
    main()
