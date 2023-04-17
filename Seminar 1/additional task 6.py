num = (input("Введите 6-ти значный номер билетика: "))
s1 = int(num[0]) + int(num[1]) + int(num[2])
s2 = int(num[3]) + int(num[4]) + int(num[5])

if s1 == s2:
    print("Этот билетик счастливый")
else:
    print("Этот билетик обычный")