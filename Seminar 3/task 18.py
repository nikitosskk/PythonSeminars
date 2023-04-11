num = int(input('Введите количество элементов списка: '))
a_entered = input("Введите через пробел элементы списка: ").split()
a_num = list(map(int, a_entered))
if len(a_num) != num or num == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число, с которым необходимо'
                  ' сравнивать элементы списка: '))
    num_min = abs(x - a_num[0])
    index = 0
    for i in range(1, num):
        count = abs(x - a_num[i])
        if count < num_min:
            num_min = count
            index = i
    print(
        f'Число {a_num[index]} в списке наиболее близко по величине к числу'
        f' {x}, их разница составляет {abs(x - a_num[index])}')
