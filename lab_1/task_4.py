#!/usr/bin/env python3

def my_reverse(x):
    return x[::-1]

def is_palindrome(s) -> bool:
    return s == my_reverse(s)

def main():
    word = input("Введите слово: ")
    print("Палиндром" if is_palindrome(word) else "Не палиндром")

if __name__ == "__main__":
    main()
