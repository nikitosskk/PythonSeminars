try:
    m = int(input("Введите номер месяца: "))
    if m < 1 or m > 12:
        raise ValueError
except ValueError:
    print("Такого месяца не существует!")

month_list = ["Зима", "Весна", "Лето", "Осень"]

if m == 12 or m == 1 or m == 2:
    print("Результат через список:", month_list[0])
elif m == 3 or m == 4 or m == 5:
    print("Результат через список:", month_list[1])
elif m == 6 or m == 7 or m == 8:
    print("Результат через список:", month_list[2])
elif m == 9 or m == 10 or m == 11:
    print("Результат через список:", month_list[3])

d = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}

if m == 12 or m == 1 or m == 2:
    print("Результат через словарь:", d[1])
elif m == 3 or m == 4 or m == 5:
    print("Результат через словарь:", d[2])
elif m == 6 or m == 7 or m == 8:
    print("Результат через словарь:", d[3])
elif m == 9 or m == 10 or m == 11:
    print("Результат через словарь:", d[4])
