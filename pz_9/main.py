# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.

def find_min_sales(sales_data):
    # Разбиваем строку на элементы
    elements = sales_data.split()
    
    products = {}
    current_product = None
    
    for elem in elements:
        if elem.isalpha():
            # Это название продукта
            current_product = elem
            products[current_product] = []
        else:
            # Это число продаж
            if current_product is not None:
                products[current_product].append(int(elem))
    
    # Находим минимальные продажи для каждого продукта
    min_sales = {}
    for product, sales in products.items():
        min_sales[product] = min(sales) if sales else 0
    
    return min_sales

# Исходная строка
data = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'

# Получаем минимальные продажи
result = find_min_sales(data)

# Выводим результат
for product, min_sale in result.items():
    print(f"{product}: {min_sale} кг")