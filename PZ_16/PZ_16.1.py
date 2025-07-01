# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.
import random

class Matrix:
    def __init__(self, rows, cols, min_val=0, max_val = 103):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера для сложения")

        result = Matrix(self.rows, self.cols)
        for i in range(self.cols):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера для вычитания")

        result = Matrix(self.rows, self.cols)
        for i in range(self.cols):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(rows.cols):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other.data[i][j]
            return result
        elif isinstance(other, Matrix):
            if self.cols != self.rows:
                raise ValueError("Количество столбцов первой матрицы должно быть равно количеству второй матрицы")

            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise TypeError("Можно умножить матрицу только на другую матрицу")


rows1 = int(input("Введите количество строк первой матрицы: "))
cols1 = int(input("Введите количество столбцов первой матрицы: "))
m1 = Matrix(rows1, cols1)

rows2 = int(input("Введите количество строк второй матрицы: "))
cols2 = int(input("Введите количество столбцов второй матрицы: "))
m2 = Matrix(rows1, cols1)

print("\Матрица 1: ")
print(m1)

print("\Матрица 2: ")
print(m2)

if m1.rows == m2.rows and m1.cols == m2.cols:
    print("\Сложение матриц: ")
    print(m1 + m2)

    print("\Вычитание матриц: ")
    print(m1 - m2)

if m1.cols == m2.rows:
    print("\Умножение матриц: ")
    print(m1 * m2)