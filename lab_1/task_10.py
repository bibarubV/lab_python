#!/usr/bin/env python3

from datetime import date

# я забыл про calendar.isleap()
def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def is_birthday(birth_date):
    today = date.today()
    # если день рождения 29 февраля, а текущий год невисокосный, то принимаем 1 марта за др
    if (birth_date.month == 2 and birth_date.day == 29) and not is_leap_year(today.year):
        return today.month == 3 and today.day == 1
    return birth_date.day == today.day and birth_date.month == today.month


def get_age(birth_date):
    today = date.today()
    diff = today.year-birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        diff -= 1
    return diff

def get_discount(birth_date, is_vip, total):
    discount = 0
    if total > 1000:
        discount += 10
    if get_age(birth_date) >= 63:
        discount += 5
    if is_birthday(birth_date):
        discount += 5
    if is_vip:
        discount = max(discount, 15)

    discount = min(discount, 25) # ???

    return discount

def main():
    # из task_6
    birth_date_str = input("Введите дату рождения покупателя (DD.MM.YYYY): ")
    day, month, year = (int(x) for x in birth_date_str.split(".", 3))
    birth_date = date(year, month, day)

    yn = input("Покупатель VIP? (д/н): ").lower()
    is_vip = yn in "yд"
    total = int(input("Введите сумму покупки: "))

    print("Рассчитанная скидка: "+str(get_discount(birth_date, is_vip, total))+"%")

if __name__ == "__main__":
    main()
