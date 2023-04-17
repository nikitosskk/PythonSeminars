"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
# Представление слов в буквенном формате
word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(list(word_1))
print(list(word_2))
print(list(word_3))
print(type(word_1))
print(type(word_2))
print(type(word_3))
# Представление слов в наборе кодовых точек Unicode
unicode_word_1 = [ord(letter) for letter in word_1]
unicode_word_2 = [ord(letter) for letter in word_2]
unicode_word_3 = [ord(letter) for letter in word_3]
print(unicode_word_1)
print(unicode_word_2)
print(unicode_word_3)
print(type(unicode_word_1))
print(type(unicode_word_2))
print(type(unicode_word_3))