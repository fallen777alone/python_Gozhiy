# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных
# последовательностях.

import random

# Генерация последовательности случайных чисел
N = int(input("Введите количество чисел в последовательности: "))
random_sequence = [random.randint(-100, 100) for _ in range(N)]

print("\nИсходная последовательность:")
print(random_sequence)

# Разделение на четные и нечетные числа
even_numbers = [x for x in random_sequence if x % 2 == 0]
odd_numbers = [x for x in random_sequence if x % 2 != 0]

print("\nЧетные числа:")
print(even_numbers)
print("\nНечетные числа:")
print(odd_numbers)

# Вычисление средних арифметических
avg_even = sum(even_numbers) / len(even_numbers) if even_numbers else 0
avg_odd = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

print("\nРезультаты:")
print(f"Среднее арифметическое четных чисел: {avg_even:.2f}")
print(f"Среднее арифметическое нечетных чисел: {avg_odd:.2f}")