# 2. Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку между второй и
# третьей.

# Чтение исходного файла
with open('pz_11/text18-7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Вывод содержимого файла
print("Содержимое файла:")
print(''.join(lines))

# Подсчет букв в нижнем регистре
lowercase_count = sum(1 for line in lines for char in line if char.islower())
print(f"\nКоличество букв в нижнем регистре: {lowercase_count}")

# Обработка стихотворения (перемещение последней строки между второй и третьей)
if len(lines) >= 3:
    modified_lines = lines[:2] + [lines[-1]] + lines[2:-1]
else:
    modified_lines = lines  # если строк меньше 3, оставляем как есть

# Создание нового файла
with open('pz_11/modified_poem_2.txt', 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

print("\nНовый файл 'modified_poem_2.txt' создан с измененным порядком строк.")