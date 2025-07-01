#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#Исходные данные:
#Количество элементов:
#Индекс максимального элемента:
#Меняем местами первую и последнюю трети:
file_ = open('PZ11/text.txt', 'w')
num = 5, 10, 11, -7, -10, -4
file_.write(str(num))
file_.close()

file = open('PZ11/text.txt', 'r')
data = file.read()
print('Содержимое текстового файла (исходные данные):', data)
elements = [num for num in data.split(', ')]
count = len(elements)
print('Количество элементов:', count)
print('Индекс максимального элемента (Число 11):', elements.index(max(elements)))
delenie_treti = count // 3
swap = elements[-delenie_treti:] + elements[delenie_treti:-delenie_treti] + elements[:delenie_treti]
print('Меняем местами первую и последнюю трети:', swap)
file.close()

file = open('PZ11/text_.txt', 'w')
numbers = 5, 10, 11, -7, -10, -4
file.write('Содержимое текстового файла (исходные данные):', )
file.write("Исходные данные:")
file.write(str(data) + '\n')
file.write("Количество элементов:")
file.write(str(count) + '\n')
file.write("Индекс максимального элемента:")
file.write(str(elements.index(max(elements))) + '\n')
file.write("Меняем местами первую и последнюю трети:")
file.write(str(swap))
print("Данные записаны в файл text_.txt")
file.close()

