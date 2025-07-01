#В матрице элементы второго столбца заменить элементами
#из одномерного динамического массива соответствующей размерности.
import random
matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица:")

for row in matrix:
    print(row)

spisok = [random.randint(1, 10) for _ in range(3)]
print("Одномерный динамический массив:", spisok)

new_matrix = list(map(lambda x, y: [x[0], spisok[y], x[2]], matrix, range(len(matrix))))
print("Матрица после замены:")

for row in new_matrix:
    print(row)


