#!/usr/bin/env python3

def password_ok(password: str) -> bool:
    return len(password) >= 16 and not password.isalnum()

def main():
    password = input("Введите ваш пароль: ")
    print("Надежный пароль" if password_ok(password) else "Слабый пароль")

if __name__ == "__main__":
    main()
