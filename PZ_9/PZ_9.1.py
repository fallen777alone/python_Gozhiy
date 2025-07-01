#  Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.

list = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'

items = list.split()

sales_data = {}
current = None
for item in items:
    if item.isalpha():
        current = item
        sales_data[current] = []
    else:
        sales_data[current].append(int(item))

min_sales = {k: min(v) for k, v in sales_data.items()}

print("Минимальные прдажи:")
for product, m in min_sales.items():
    print(f"{product}: {m} кг")