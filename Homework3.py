# 1. Запитуємо перше число
try:
    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))
    if operation == "+":
        print("Результат:", num1 + num2)
    elif operation == "-":
        print("Результат:", num1 - num2)
    elif operation == "*":
        print("Результат:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Помилка! Ділення на нуль неможливе.")
        else:
            print("Результат:", num1 / num2)
except ValueError:
    print("Помилка: Ви ввели не число. Вводьте тільки цифри.")