# Подcчитать четные и нечетные цифры введенного натурального числа с помощью
# рекурсии.

def count_even_odd(n, even=0, odd=0):
    if n == 0:
        print(
            f"Количество четных и нечетных цифр в числе равно:"
            f" ({even}, {odd})")
        return
    else:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        count_even_odd(n // 10, even, odd)


num = int(input("Введите число: "))
count_even_odd(num)
