#!/usr/bin/env python3

from datetime import date
from calendar import isleap

# western variant II
# https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4#%D0%93%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%B8%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D0%BB%D0%B5%D0%BD%D0%B4%D0%B0%D1%80%D1%8C
def astrological_sign(days: int, leap: bool) -> str:
    if leap and days >= 60:
        days -= 1
    if days < 1 or days > 365:
        raise ValueError("недопустимое значение дня в году")
    if days >= 357 or days <= 20:
        return "♑ (Козерог)"
    elif days <= 50:
        return "♒ (Водолей)"
    elif days <= 79:
        return "♓ (Рыбы)"
    elif days <= 110:
        return "♈ (Овен)"
    elif days <= 141:
        return "♉ (Телец)"
    elif days <= 172:
        return "♊ (Близнецы)"
    elif days <= 203:
        return "♋ (Рак)"
    elif days <= 233:
        return "♌ (Лев)"
    elif days <= 266:
        return "♍ (Дева)"
    elif days <= 296:
        return "♎ (Весы)"
    elif days <= 326:
        return "♏ (Скорпион)"
    else:
        return "♐ (Стрелец)"

def main():
    birth_date_str = input("Введите дату рождения (DD.MM.YYYY): ")
    #birth_date = date.strptime(birth_date_str, "%d.%m.%y") # для этого день и месяц должны быть из двух цифр
    day, month, year = (int(x) for x in birth_date_str.split(".", 3))
    birth_date = date(year, month, day)
    sign = astrological_sign(birth_date.timetuple().tm_yday, isleap(birth_date.year))
    print("Ваш знак зодиака: "+sign)

if __name__ == "__main__":
    main()
