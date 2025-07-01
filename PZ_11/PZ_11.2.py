#  Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку между второй и третьей

def read_file(filename):
    with open(filename, 'r', encoding='utf-16') as file:
        return file.read()

def count_lowercase(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    return count

def process_poem(text, output_filename):
    lines = text.split('\n')
    if len(lines) >= 3:
        new_lines = []
        new_lines.extend(lines[:2])
        new_lines.append(lines[-1])
        new_lines.extend(lines[2:-1])

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
        return True
    return False

content = read_file('text18-7.txt')
print(f"Содержимое файла:\n{content}\n")
print(f"Букв в нижнем регистре: {count_lowercase(content)}")

if process_poem(content, 'processed_poem.txt'):
    print("Файл успешно обработан")
else:
    print("Файл слишком короткий для обработки")