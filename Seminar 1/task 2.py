a = int(input('Введите время в секундах:'))

seconds = a % (24 * 3600)
hours = a // 3600
seconds %= 3600
minutes = a // 60
seconds %= 60

print("Количество часов равно ", hours)
print("Количество минут равно ", minutes)
print("%02d:%02d:%02d" % (hours, minutes, seconds))