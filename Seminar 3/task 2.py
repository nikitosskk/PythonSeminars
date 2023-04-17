my_list = [7, 5, 3, 3, 2]

try:
    num = int(input("Введите новый элемент рейтинга: "))
except ValueError:
    print("Введите целое число")

if num >= 7:
    my_list.insert(0, num)
    print(f"Пользователь ввел число {num}. Результат: {my_list}")
elif num == 6:
    my_list.insert(1, num)
    print(f"Пользователь ввел число {num}. Результат: {my_list}")
elif num == 5 or num == 4:
    my_list.insert(2, num)
    print(f"Пользователь ввел число {num}. Результат: {my_list}")
elif num == 3:
    my_list.insert(4, num)
    print(f"Пользователь ввел число {num}. Результат: {my_list}")
elif num <= 2:
    my_list.insert(5, num)
    print(f"Пользователь ввел число {num}. Результат: {my_list}")


