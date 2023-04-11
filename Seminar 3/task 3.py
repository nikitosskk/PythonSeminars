goods = []
i = 1

while True:
    name = input("Введите название товара или стоп для завершения ввода: ")
    if name.lower() == "стоп":
        break
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения товара: ")
    goods.append((i, {"Название товара": name,
                      "цена": price,
                      "количество": quantity,
                      "eд.": unit}))
    i += 1

analytics = {}
for name, value in goods[0][1].items():
    analytics[name] = [item[1][name] for item in goods]

print("Структура товаров:")
print(goods)
print("Аналитика товаров:")
print(analytics)
