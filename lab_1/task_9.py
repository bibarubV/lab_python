#!/usr/bin/env python3

categories = [
    ("Длина", {
            "мм": 1e-3, "см": 1e-2, "дм": 1e-1, "м": 1,
            "км": 1e3, "дюйм": 0.0254, "фут": 0.3048,
            "ярд": 0.9144, "миля": 1609.344,
        }
    ),
    ("Масса", { # кг базовые как в си
            "мг": 1e-6, "г": 1e-3, "кг": 1, "т": 1e3,
            "фунт": 0.453592, "унция": 0.0283495
        }
    ),
    ("Температура", { # handled in convert_temperature()
            "Цельсий": None, "Фаренгейт": None, "Кельвин": None,
        }
    ),
    ("Время", {
            "с": 1, "мин": 60, "час": 60*60,
            "сутки": 60*60*24, "неделя": 60*60*24*7, "год": 60*60*24*365,
        }
    ),
    ("Площадь", {
            "мм²": 1e-6, "см²": 1e-4, "м²": 1, "км²": 1e6,
            "гектар": 1e4, "акр": 4046.86,
        }
    ),
    ("Объем", {
            "мл": 1e-3, "л/дм³": 1, "м³": 1e3,
            "галлон": 3.78541, "пинта": 0.473176,
        }
    ),
    ("Скорость", {
            "м/с": 1, "км/ч": 1/3.6, "миль/ч": 0.44704, "узел": 0.514444,
        }
    ),
    ("Давление", {
            "Па": 1, "кПа": 1e3, "бар": 1e5,
            "атм": 101325, "мм рт.ст.": 133.322,
        }
    ),
    ("Энергия", {
            "Дж": 1, "кДж": 1e3, "кал": 4.184,
            "ккал": 4.184e3, "кВт·ч": 1e3*60*60,
        }
    ),
    ("Данные", {
            "байт": 1,
            "КиБ": 1<<10, "МиБ": 1<<20, "ГиБ": 1<<30, "ТиБ": 1<<40,
            "КБ": 1e3, "МБ": 1e6, "ГБ": 1e9, "ТБ": 1e12,
        }
    ),
    ("Угол", {
            "градус": 1, "радиан": 57.2958, "градиан": 0.9,
        }
    ),
]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Цельсий":
        celsius = value
    elif from_unit == "Фаренгейт":
        celsius = (value-32)*5/9
    elif from_unit == "Кельвин":
        celsius = value-273.15
    else:
        raise TypeError("неподдерживаемая единица температуры на входе")

    if to_unit == "Цельсий":
        return celsius
    elif to_unit == "Фаренгейт":
        return celsius*9/5+32
    elif to_unit == "Кельвин":
        return celsius+273.15
    else:
        raise TypeError("неподдерживаемая единица температуры на выходе")

def main():
    for i, t in enumerate(categories):
        print(f"{i}. {t[0]}")

    choice = int(input("\nВыберите тип измерения: "))

    category_name, units = categories[choice]

    print(f"\n--- {category_name} ---")
    unit_list = list(units.keys())
    for i, u in enumerate(unit_list):
        print(f"{i}. {u}")

    from_i = int(input("\nИз какой единицы (номер): "))
    to_i = int(input("В какую единицу (номер): "))

    from_unit = unit_list[from_i]
    to_unit = unit_list[to_i]

    value_str = input(f"\nВведите значение в \"{from_unit}\": ").strip().replace(",", ".")
    value = float(value_str)

    if from_unit == to_unit:
        result = value
    elif category_name == "Температура":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        base_value = value * units[from_unit]
        result = base_value / units[to_unit]

    print(f"\n{value_str} {from_unit} = {result:g} {to_unit}")

if __name__ == "__main__":
    main()
