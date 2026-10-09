#!/usr/bin/env python3

def format_name(name: str) -> str:
    if isinstance(name, str):
        last, first, middle = name.split(maxsplit=2)
        return f"{last} {first[0]}. {middle[0]}."
    elif isinstance(name, tuple) or isinstance(name, list):
        return f"{name[0]} {name[1][0]}. {name[2][0]}."
    else:
        raise Exception("неправильно введено фио")

def main():
    # фио одной строкой
    name = input("Введите ФИО: ")
    print("Вы "+format_name(name))

    # фио тремя строками
    last = input("Введите фамилию: ")
    first = input("Введите имя: ")
    middle = input("Введите отчество: ")
    print("Вы "+format_name(name))

if __name__ == "__main__":
    main()
