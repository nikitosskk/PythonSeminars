x = int(input("Введите первое число"))
y = int(input("Введите второе число"))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)