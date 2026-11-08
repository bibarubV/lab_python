#!/usr/bin/env python3

from datetime import date

class Buyer:
    def __init__(self, birth_date, is_vip):
        self.birth_date = birth_date
        self._is_vip = is_vip

    # я забыл про calendar.isleap()
    @staticmethod
    def is_leap_year(year):
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

    def is_birthday(self):
        today = date.today()
        # если день рождения 29 февраля, а текущий год невисокосный, то принимаем 1 марта за др
        if (self.birth_date.month == 2 and self.birth_date.day == 29) and not self.is_leap_year(today.year):
            return today.month == 3 and today.day == 1
        return self.birth_date.day == today.day and self.birth_date.month == today.month

    def get_age(self):
        today = date.today()
        diff = today.year-self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            diff -= 1
        return diff

    def is_vip(self):
        return self._is_vip

class Discount:
    def __init__(self, buyer, total):
        self.buyer = buyer
        self.total = total

    def get_discount(self):
        discount = 0
        if self.total > 1000:
            discount += 10
        if self.buyer.get_age() >= 63:
            discount += 5
        if self.buyer.is_birthday():
            discount += 5
        if self.buyer.is_vip():
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

    print("Рассчитанная скидка: "+str(Discount(Buyer(birth_date, is_vip), total).get_discount())+"%")

if __name__ == "__main__":
    main()
