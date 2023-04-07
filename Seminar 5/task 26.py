# Напишите программу, которая на вход принимает два чиcла A и B, и возводит
# число А в целую степень B с помощью рекурсии.
from math import pow


def num_degrees(n1, n2):
    if n2 == 0:
        return 1
    elif n2 == 1:
        return n1
    else:
        return n1 * num_degrees(n1, n2 - 1)


num1, num2 = int(input("Введите число A: ")), int(input("Введите степень B: "))
print(f"Число {num1} в степени {num2} => {num_degrees(num1, num2)}")
