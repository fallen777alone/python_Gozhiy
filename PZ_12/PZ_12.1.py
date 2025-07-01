# 1.Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных
# последовательностях.

import random
from functools import reduce

def generate_random_sequence(n):
    return[random.randint(1, 100) for _ in range(n)]
def split_sequence(seq):
    even = list(filter(lambda x: x % 2 == 0, seq))
    odd = list(filter(lambda x: x % 2 != 0, seq))
    return even, odd

def calculate_average(seq):
    return reduce(lambda a, b: a + b, seq, 0) / len(seq) if seq else 0

n = int(input("Введите количество чисел N: "))
sequence = generate_random_sequence(n)

print("Исходная последовательность:", sequence)

even_seq, odd_seq = split_sequence(sequence)

print("Четные числа", even_seq)
print("Нечетные числа", odd_seq)

avg_even = calculate_average(even_seq)
avg_odd = calculate_average(odd_seq)

print("Среднее арифмитическое четных чисел:", avg_even)
print("Среднее арифмитическое нечетных чисел:", avg_odd)