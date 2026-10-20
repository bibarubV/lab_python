#!/usr/bin/env python3

import random

def main():
    val = random.randint(1, 100)
    while True:
        x = int(input("Угадайте число: "))
        if x == val:
            print("Верно!")
            break
        elif val > x:
            print("Больше")
        elif val < x:
            print("Меньше")

if __name__ == "__main__":
    main()
