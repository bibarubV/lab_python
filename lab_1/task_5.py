#!/usr/bin/env python3

def num(x):
    x = x.replace(",", ".")
    return float(x) if "." in x else int(x)

def main():
    a = num(input("Введите число a: "))
    b = num(input("Введите число b: "))
    print("a + b = "+str(a+b))
    print("a - b = "+str(a-b))
    print("a * b = "+str(a*b))
    if b != 0:
        # целочисленное деление, если оба числа были введены как целые, иначе дробное
        if isinstance(a, int) and isinstance(b, int):
            print("a // b = "+str(a//b))
            print("a % b = "+str(a%b))
        else:
            print("a / b = "+str(a/b))
    print("a ^ b = "+str(a**b))

if __name__ == "__main__":
    main()
