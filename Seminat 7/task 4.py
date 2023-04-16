# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод init()), который должен принимать данные (список списков) для
# формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += ' '.join(str(elem) for elem in row) + '\n'
        return result

    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(
                other.data[0]):
            raise ValueError('Matrices must be of the same size.')
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])
m3 = m1.add(m2)
print(m1)
print(m2)
print(m3)