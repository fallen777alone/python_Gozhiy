# 1. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
import random

def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    return[[random.randint(1,9) for _ in range(cols)] for _ in range(rows)]

def increase_row(matrix, n, value=3):
    return[
        list(map(lambda x: x + value if i == n else x, row))
        for i, row in enumerate(matrix)
    ]

print("Ввод матрицы:")
matrix = input_matrix()

n = int(input("Введите номер строки (Начиная с 0): "))

if n < 0 or n >= len(matrix):
    print("Ошибка: неверный номер строки")
else:
    new_matrix = increase_row(matrix, n)
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    print(f"\nМатрица после увеличения строки {n} на 3:")
    for row in new_matrix:
        print(row)
