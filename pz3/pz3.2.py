def convert_to_kilograms(unit, mass):
    if unit == 1:  # килограмм
        return mass
    elif unit == 2:  # миллиграмм
        return mass / 1000000
    elif unit == 3:  # грамм
        return mass / 1000
    elif unit == 4:  # тонна
        return mass * 1000
    elif unit == 5:  # центнер
        return mass * 100
    else:
        return None

# Тестирование
print("\nЗадача 2: Конвертация массы в килограммы")
print("=" * 50)

# Список единиц измерения
units = {
    1: "килограмм",
    2: "миллиграмм", 
    3: "грамм",
    4: "тонна",
    5: "центнер"
}

# Примеры
test_cases = [
    (1, 5.0),    # 5 кг
    (2, 5000.0), # 5000 мг
    (3, 2500.0), # 2500 г
    (4, 2.5),    # 2.5 т
    (5, 3.0)     # 3 ц
]

print("Примеры конвертации:")
for unit, mass in test_cases:
    result = convert_to_kilograms(unit, mass)
    unit_name = units[unit]
    print(f"{mass} {unit_name} = {result} кг")

# Интерактивный ввод
print("\n" + "=" * 50)
print("Доступные единицы измерения:")
print("1 - килограмм")
print("2 - миллиграмм") 
print("3 - грамм")
print("4 - тонна")
print("5 - центнер")

unit = int(input("Выберите номер единицы измерения (1-5): "))
mass = float(input("Введите массу: "))

result = convert_to_kilograms(unit, mass)
if result is not None:
    unit_name = units[unit]
    print(f"{mass} {unit_name} = {result} килограмм")
else:
    print("Ошибка: неверный номер единицы измерения")