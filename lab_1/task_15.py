#!/usr/bin/env python3

from collections import defaultdict

# в этом задании считаю разными позиции с одинаковым называнием но разной ценой
sales = [
    {"name": "Nintendo Switch 2", "price": 500, "sold": 10},
    {"name": "Sony Playstation 5", "price": 650, "sold": 10},
    {"name": "Xbox Series X", "price": 800, "sold": 4},
    {"name": "Sony Playstation 5", "price": 650, "sold": 3},
    {"name": "Xbox Series S", "price": 500, "sold": 2},
]

def input_sale_info(sales_list):
    name = input("Введите наименование товара: ")
    price = int(input("Введите цену товара: "))
    sold = int(input("Введите количество проданных единиц: "))
    sales_list.append({"name": name, "price": price, "sold": sold})

def merge_sales(sales_list):
    temp_sales_dict = defaultdict(int)
    for x in sales_list:
        t = (x["name"], x["price"])
        temp_sales_dict[t] += x["sold"]
    new_sales_list = []
    for k, v in temp_sales_dict.items():
        new_sales_list.append({"name": k[0], "price": k[1], "sold": v})
    return new_sales_list

def analyze_sales(sales_list):
    revenue = defaultdict(int)
    #sales_list = merge_sales(sales_list)
    #print("Уникальных товарных позиций: ", len(sales_list))
    for x in sales_list:
        t = (x["name"], x["price"])
        revenue[t] += x["sold"]*x["price"]
    max_revenue_item = max(revenue, key=revenue.get)
    print("Уникальных товарных позиций: ", len(revenue))
    print("Самый прибыльный товар: "+str(max_revenue_item[0])+" ("+str(max_revenue_item[1])+") - выручка "+str(revenue[max_revenue_item]))
    print("Выручка по всем товарам:")
    for k, v in revenue.items():
        print(k[0]+" ("+str(k[1])+"): "+str(v))
    

def main():
    analyze_sales(sales)

if __name__ == "__main__":
    main()
