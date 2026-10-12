#!/usr/bin/env python3

def num(x):
    return float(x) if "." in x else int(x)

def main():
    a_ = input("Введите число a: ")
    a = num(a_)
    b_ = input("Введите число b: ")
    b = num(b_)
    print("a+b = "+str(a+b))
    print("a-b = "+str(a-b))
    print("a*b = "+str(a*b))
    if b != 0:
        print("a // b = "+str(a//b))
        print("a % b = "+str(a%b))
    print("a^b = "+str(a**b))

if __name__ == "__main__":
    main()
