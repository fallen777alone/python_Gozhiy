# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:

import random

list = [random.randint(1, 40) for _ in range(7)]
slist = (str(list))
total_count = 0
total_sum = 0
positive_list = []

op = open('data_1.txt', 'w')
op.writelines(slist)
op.close()

op2 = open('data_2.txt', 'w')
op2.write('Исходные данные: ')
op2.write('\n')
op2.writelines(slist)
op2.close()

op = open('data_1.txt')
o = op.read()
o = o.split()
for i in range(len(o)):
    total_count += 1
    total_sum += i
    if i > 0 and i % 2 == 0:
        positive_list.append(i)

average_all = total_sum / total_count if total_count > 0 else 0

positive_count = len(positive_list)
positive_sum = sum(positive_list)
positive_average = positive_sum / positive_count if positive_count > 0 else 0


op2 = open('data_2.txt', 'a')
op2.write('\n')
print('Количество элементов: ', total_count,
      'Среднее арифметическое элементов: ', average_all,
      'Положительные четные элементы: ', positive_list ,
      'Сумма положительных четных элементов: ', positive_sum,
      'Среднее арифметическое положительных четных элементов: ', positive_average,
      file=op2)
op2.close()