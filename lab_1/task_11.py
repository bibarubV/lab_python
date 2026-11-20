#!/usr/bin/env python3

from math import inf

def assess_credit_risk(age, monthly_income, loan_amount, loan_term, credit_history, has_guarantors, has_collateral):
    total_income_for_term = monthly_income*loan_term
    dti = loan_amount/total_income_for_term if total_income_for_term > 0 else inf
    monthly_payment = loan_amount/loan_term
    payment_to_income = monthly_payment/monthly_income if monthly_income > 0 else inf

    score = 100  # стартовый балл (100 = минимальный риск)

    if age < 21:
        score -= 25
    elif age < 25:
        score -= 10
    elif age > 65:
        score -= 20
    elif age > 60:
        score -= 10

    if credit_history == "отличная":
        pass
    elif credit_history == "хорошая":
        score -= 10
    elif credit_history == "удовлетворительная":
        score -= 25
    elif credit_history == "плохая":
        score -= 45
    else:
        raise ValueError("недопустимое значение кредитной истории")

    if dti > 3.:
        score -= 35
    elif dti > 2.:
        score -= 20
    elif dti > 1.:
        score -= 10

    if payment_to_income > .7:
        score -= 30
    elif payment_to_income > .5:
        score -= 20
    elif payment_to_income > .4:
        score -= 10

    if has_guarantors:
        score += 10
    if has_collateral:
        score += 15

    score = max(0, min(100, score))

    if score >= 75:
        risk = "Низкий"
        rate = 12.
    elif score >= 55:
        risk = "Средний"
        rate = 17.
    elif score >= 30:
        risk = "Высокий"
        rate = 24.
    else:
        risk = "Критический"
        rate = 32.

    if loan_term > 60:
        rate += 1.5
    elif loan_term > 36:
        rate += .5
    if has_collateral:
        rate -= 2.
    if has_guarantors:
        rate -= 1.
    rate = max(rate, 8.)

    if risk == "Критический":
        decision = "ОТКЛОНИТЬ"
        comment = "Слишком высокий уровень риска. Рекомендуется отказ."
    elif risk == "Высокий":
        if has_collateral and has_guarantors:
            decision = "ОДОБРИТЬ С УСЛОВИЯМИ"
            comment = "Высокий риск, но наличие залога и поручителей снижает угрозу."
        else:
            decision = "ТРЕБУЕТСЯ ДОПОЛНИТЕЛЬНОЕ ОБЕСПЕЧЕНИЕ"
            comment = "Высокий риск. Требуется дополнительное обеспечение."
    elif risk == "Средний":
        decision = "ОДОБРИТЬ С УСЛОВИЯМИ"
        comment = "Средний риск. Возможно одобрение с повышенной ставкой."
    else:
        decision = "ОДОБРИТЬ"
        comment = "Низкий риск. Заявка может быть одобрена на стандартных условиях."

    return {
        "Балл": score,
        "DTI (кредит/доход за срок)": round(dti, 2),
        "Платёж/доход (в месяц)": round(payment_to_income, 2),
        "Категория риска": risk,
        "Процентная ставка": f"{rate:.1f}%",
        "Решение": decision,
        "Рекомендация": comment
    }

def main():
    age = int(input("Введите возраст заемщика: "))
    monthly_income = int(input("Введите ежемесячный доход: "))
    loan_amount = int(input("Введите размер кредита: "))
    loan_term = int(input("Введите срок кредита (месяцы): "))
    credit_history = input("Введите кредитную историю (отличная/хорошая/удовлетворительная/плохая): ").lower()
    has_guarantors = input("Есть поручители? (д/н): ").lower() in "yд"
    has_collateral = input("Есть залог? (д/н): ").lower() in "yд"
    result = assess_credit_risk(age, monthly_income, loan_amount, loan_term, credit_history, has_guarantors, has_collateral)
    for k, v in result.items():
        print(str(k)+": "+str(v))

if __name__ == "__main__":
    main()
