#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
#миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
#число в диапазоне 1-5) и масса тела в этих единицах (вещественное число). Найти
#массу тела в килограммах.

def convert_to_kilograms(unit, mass):
    if unit == 1:  
        return mass
    elif unit == 2:  
        return mass / 1000000
    elif unit == 3:  
        return mass / 1000
    elif unit == 4: 
        return mass * 1000
    elif unit == 5:  
        return mass * 100
    else:
        return None



units = {
    1: "килограмм",
    2: "миллиграмм", 
    3: "грамм",
    4: "тонна",
    5: "центнер"
}


test_cases = [
    (1, 5.0),  
    (2, 5000.0), 
    (3, 2500.0), 
    (4, 2.5),    
    (5, 3.0)  
]

print("Примеры конвертации:")
for unit, mass in test_cases:
    result = convert_to_kilograms(unit, mass)
    unit_name = units[unit]
    print(f"{mass} {unit_name} = {result} кг")


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
