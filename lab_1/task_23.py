#!/usr/bin/env python3

from math import ceil

categories = ("Жилье", "Питание", "Транспорт", "Развлечения", "Прочее")

def comma_float_input(s):
    return float(input(s).replace(",", "."))

def main():
    # предполагается что ввод всего положительный
    income = comma_float_input("Введите доход за месяц в рублях: ")

    expenses = {}
    print("\nВведите расходы по категориям")
    for category in categories:
        expenses[category] = comma_float_input(category+": ")

    total_expenses = sum(expenses.values())
    remaining = income-total_expenses
    remaining_rate = remaining_rate = remaining/income*100 if income > 0 else 0

    print(f"Всего расходов: {total_expenses:.2f} руб.")
    print(f"Остаток: {remaining:.2f} руб. ({remaining_rate:.1f}% дохода)")

    print("\nДоли расходов:")
    if total_expenses:
        for category, amount in expenses.items():
            pct = amount/total_expenses*100
            print(f"{category}: {amount:.2f} руб. ({pct:.1f}%)")
    else:
        print("Расходов нет.")

    print("\nРекомендации: ", end="")
    if remaining < 0:
        print("Расходы превышают доходы, сократите траты на развлечения.")
    elif remaining_rate < 20:
        print("Количество сбережений ниже нормы, попробуйте урезать второстепенные расходы.")
    else:
        print("Отличный баланс.")

    if total_expenses:
        top_category = max(expenses, key=expenses.get)
        print(f"Главная статья расходов: {top_category} ({expenses[top_category]:.2f} руб.).")

    print("\nПланирование крупной покупки")
    goal_name = input("На что хотите накопить? ")
    goal_cost = comma_float_input("Сколько это стоит (руб)? ")

    if remaining > 0:
        months = ceil(goal_cost/remaining)
        print(f"При текущих сбережениях вы накопите на {goal_name} за {months} мес.")
    else:
        print(f"Вы не откладываете деньги, накопить на {goal_name} сейчас невозможно.")

if __name__ == "__main__":
    main()
