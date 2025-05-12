# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:

# Формируем исходный файл с числами
with open('pz_11/numbers_1.txt', 'w', encoding='utf-8') as f:
    f.write("-5 12 -8 7 14 0 -3 6 9 -10 4 11 -2 5 -7")

# Читаем данные из файла и обрабатываем их
with open('pz_11/numbers_1.txt', 'r', encoding='utf-8') as f:
    numbers = list(map(int, f.read().split()))

# Вычисляем требуемые значения
count = len(numbers)
average = sum(numbers) / count if count > 0 else 0
positive_even = [x for x in numbers if x > 0 and x % 2 == 0]
sum_positive_even = sum(positive_even)
average_positive_even = sum_positive_even / len(positive_even) if positive_even else 0

# Формируем новый файл с результатами
with open('pz_11/results_1.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные: " + ' '.join(map(str, numbers)) + '\n')
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Среднее арифметическое элементов: {average:.2f}\n")
    f.write(f"Положительные четные элементы: {' '.join(map(str, positive_even))}\n")
    f.write(f"Сумма положительных четных элементов: {sum_positive_even}\n")
    f.write(f"Среднее арифметическое положительных четных элементов: {average_positive_even:.2f}\n")

print("Файл с результатами успешно создан в папке results_1.txt")