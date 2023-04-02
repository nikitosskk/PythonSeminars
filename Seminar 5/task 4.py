# Найти cумму n элементов следующего ряда чисел с помощью рекурсии:

def sum_series(n):
    if n == 1:
        return 1
    else:
        return ((-1) ** (n + 1) * 0.5 ** (n - 1)) + sum_series(n - 1)


n = int(input("Введите количество элементов: "))
result = sum_series(n)
print("Количество элементов -", n, ", их сумма -", result)
