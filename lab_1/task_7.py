#!/usr/bin/env python3

def format_div_hundred(x):
    return f"{x//100},{x%100:02}"

tax = 2 # %

def calculate_price(basic_units, unit_price, units):
    if units < 0:
        raise ValueError("количество единиц не может быть отрицательным")
    return 0 if units <= basic_units else (units-basic_units)*unit_price

def bill(minutes, messages, data):
    base_price = 2499
    print("Базовая тарификация: "+format_div_hundred(base_price))
    messages_price = calculate_price(30, 59, messages)
    if messages_price:
        print("Сумма за доп. сообщения: "+format_div_hundred(messages_price))
    minutes_price = calculate_price(60, 89, minutes)
    if minutes_price:
        print("Сумма за доп. минуты: "+format_div_hundred(minutes_price))
    data_price = calculate_price(1000, 79, data)
    if data_price:
        print("Сумма за доп. трафик: "+format_div_hundred(data_price))
    total = base_price+messages_price+minutes_price+data_price
    print("Итого: "+format_div_hundred(total))
    tax_added = round(total*tax/100)
    print("Налог "+str(tax)+"%: "+format_div_hundred(tax_added))
    total_taxed = total+tax_added
    print("Итого с учетом налога: "+format_div_hundred(total_taxed))
    return total

def main():
    minutes = int(input("Введите количество минут разговора: "))
    messages = int(input("Введите количество отправленных сообщений: "))
    data = int(input("Введите количество интернет-трафика: "))
    bill(minutes, messages, data)

if __name__ == "__main__":
    main()
