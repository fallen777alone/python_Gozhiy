#  В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
years = re.findall(r'\b(18[0-9]{2})\s+(?:год[ауе]?|году)\b', text, re.IGNORECASE)

print("Найденные годы:")
for year in years:
    print(year)

print(f"\nВсего найдено: {len(years)}")