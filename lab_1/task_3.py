#!/usr/bin/env python3

def change(val: int) -> dict[int, int]:
    notes = (100, 50, 10, 5, 2, 1)
    change = {}
    for note in notes:
        if val//note:
            change[note] = val//note
            val %= note
    return change

def main():
    val = int(input("Введите сумму: "))
    change_dict = change(val)
    
    print("Размен:")
    for k, v in change_dict.items():
        print(f"{k} рублей: {v} единицы")

if __name__ == "__main__":
    main()
