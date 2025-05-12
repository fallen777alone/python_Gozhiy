# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.

import re
import os
from pathlib import Path

def find_years(filename):
    """Находит все упоминания годов в тексте"""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Регулярное выражение для поиска годов (1821, 1837 год, 1843 году и т.д.)
    pattern = r'\b(1[0-9]{3}|20[0-9]{2})\s*(?:год[ауе]?|г\.?)?\b'
    years = re.findall(pattern, text)
    
    return years

# Создаем папку pz14, если её нет
Path("pz14").mkdir(exist_ok=True)

# Указываем путь к файлу
filename = os.path.join("pz_14", "Dostoevsky.txt")

# Проверяем существование файла
if not os.path.exists(filename):
    print(f"Ошибка: файл {filename} не найден!")
    print("Пожалуйста, убедитесь, что файл Dostoevsky.txt находится в папке pz14")
else:
    # Получаем список годов
    years = find_years(filename)
    
    # Удаляем дубликаты и сортируем
    unique_years = sorted(set(years), key=int)
    
    print("Найденные года в тексте:")
    for i, year in enumerate(unique_years, 1):
        print(f"{i}. {year}")
    
    print(f"\nВсего найдено упоминаний года: {len(years)}")
    print(f"Уникальных годов: {len(unique_years)}")
    
    # Сохраняем результаты в файл
    output_file = os.path.join("pz_14", "years_results.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Найденные года в тексте:\n")
        f.write("\n".join(f"{i}. {year}" for i, year in enumerate(unique_years, 1)))
        f.write(f"\n\nВсего упоминаний года: {len(years)}")
        f.write(f"\nУникальных годов: {len(unique_years)}")
    
    print(f"\nРезультаты сохранены в файл: {output_file}")