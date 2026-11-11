#!/usr/bin/env python3

def change(val: int) -> dict[int, int]:
    notes = (100, 50, 20, 10, 5, 2, 1) # должно быть отсортировано в порядке убывания
                                       # https://github.com/Shalvi404/Python_lab/pull/1#discussion_r4525487711
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
