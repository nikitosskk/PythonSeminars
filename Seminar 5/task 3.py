# Cформировать из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран с помощью рекурсии.

def reverse_number(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + reverse_number(n // 10)


num = int(input("Введите число, которое требуется перевернуть: "))
print(f"Перевернутое число: {reverse_number(num)}")
