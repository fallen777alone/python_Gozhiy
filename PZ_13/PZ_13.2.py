# 2. В матрице элементы последнего столбца заменить на -1.
import random

def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    return[[random.randint(1,9) for _ in range(cols)] for _ in range(rows)]


def replace_last_column(matrix, value=-1):
    return list(
        map(lambda row: list(
            map(lambda x: value if x[0] == len(row) - 1 else x[1],
                enumerate(row))
        ), matrix)
    )

print("Ввод матрицы:")
matrix = input_matrix()

new_matrix = replace_last_column(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nМатрица после замены:")
for row in new_matrix:
    print(row)