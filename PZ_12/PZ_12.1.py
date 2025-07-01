#1. Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество
import random
posled1 = [random.randint(1, 100) for _ in range(10)]
posled2 = [random.randint(1, 100) for _ in range(10)]
print('Первая последовательность:', posled1)
print('Вторая последовательность:', posled2)

common_elements = list(filter(lambda x: x in posled1, posled2))
count_common_elements = len(common_elements)

print("Общие элементы:", common_elements)
print("Количество общих элементов:", count_common_elements)