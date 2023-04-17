# Напиcать программу используя рекурсию, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.

def calculate():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation == '0':
        print("Выход из программы!")
        return
    elif operation not in ['+', '-', '*', '/']:
        print("Вы ввели неверный знак операции. Попробуйте еще раз.")
        calculate()
    else:
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Вместо числа вы ввели строку или нецелое число. "
                  "Попробуйте еще раз.")
            calculate()
        if operation == '+':
            result = num1 + num2
            print("Результат: ", result)
            calculate()
        elif operation == '-':
            result = num1 - num2
            print("Результат: ", result)
            calculate()
        elif operation == '*':
            result = num1 * num2
            print("Результат: ", result)
            calculate()
        elif operation == '/':
            if num2 == 0:
                print("На ноль делить нельзя! Попробуйте еще раз.")
                calculate()
            else:
                result = num1 / num2
                print("Результат: ", result)
                calculate()


calculate()
