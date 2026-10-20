#!/usr/bin/env python3

def format_div_hundred(x):
    return f"{x//100},{x%100:02}"

tax = 2 # %

class Service:
    def __init__(self, units, unit_price):
        self.units = units
        self.unit_price = unit_price

    def calculate_price(self, units):
        if units < 0:
            raise ValueError("количество единиц не может быть отрицательным")
        return 0 if units <= self.units else (units-self.units)*self.unit_price

class Plan:
    voice = Service(60, 89)
    sms = Service(30, 59)
    internet = Service(1000, 79)
    base_price = 2499

    @classmethod
    def bill(cls, minutes, messages, data):
        print("Базовая тарификация: "+format_div_hundred(cls.base_price))
        messages_price = cls.sms.calculate_price(messages)
        if messages_price:
            print("Сумма за доп. сообщения: "+format_div_hundred(messages_price))
        minutes_price = cls.voice.calculate_price(minutes)
        if minutes_price:
            print("Сумма за доп. минуты: "+format_div_hundred(minutes_price))
        data_price = cls.internet.calculate_price(data)
        if data_price:
            print("Сумма за доп. трафик: "+format_div_hundred(data_price))
        print("Налог: "+str(tax)+"%")
        total = cls.base_price+messages_price+minutes_price+data_price
        total *= 1+tax/100
        total = round(total)
        print(f"Итого: "+format_div_hundred(total))
        return total

def main():
    minutes = int(input("Введите количество минут разговора: "))
    messages = int(input("Введите количество отправленных сообщений: "))
    data = int(input("Введите количество интернет-трафика: "))
    Plan.bill(minutes, messages, data)

if __name__ == "__main__":
    main()
