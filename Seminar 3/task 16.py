num = int(input('Введите количество элементов списка: '))
a_elem = input("Введите через пробел элементы списка: ").split()
a_num = list(map(int, a_elem))

if len(a_num) != num:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число которое необходимо найти в списке: '))
    count = 0
    for i in range(num):
        if a_num[i] == x:
            count += 1
    print(f'Число {x} встречается в списке {count} раз')