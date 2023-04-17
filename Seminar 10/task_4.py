"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["разработка", "администрирование", "protocol", "standard"]
for word in words:
    print(word)
    print(type(word))
    b_word = str.encode(word, encoding='utf-8')
    print(b_word)
    print(type(b_word))
    s_word = bytes.decode(b_word, encoding='utf-8')
    print(s_word)
    print(type(s_word))
    print()
