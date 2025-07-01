#В исходном текстовом файле(Dostoevsky.txt) найти все варинаты фамилии Достоевского
#(т.е с различными окончаниями, например , Достоевский, Достоевского) в единственном экзампляре.
import re
with open('PZ14/Dostoevsky.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print('Содержимое файла:',
          '\n',content)
    variants = re.findall(r'Достоевск[а-я]+', content)
    unique_variants = set(variants)
    print('Уникальные варианты фамилии Достоевского:', unique_variants)


