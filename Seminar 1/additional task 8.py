n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Введите число k: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да :)')
else:
    print('Нет')