while True:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Помилка: ділення на нуль!"
    else:
        result = "Невідома операція"
    print("Результат:", result)
    cont = input("Бажаєте продовжити? (yes): ").lower()
    if cont not in ['yes']:
        print("Дякую за роботу! До побачення.")
        break