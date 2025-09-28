def check_between(a, b, c):
    if a < c:
        return a < b < c
    else:
        return c < b < a

# Тестирование
print("Задача 1: Проверка, находится ли B между A и C")
print("=" * 50)

# Пример 1
a, b, c = 5, 10, 15
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")

# Пример 2
a, b, c = 20, 15, 10
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")

# Пример 3
a, b, c = 10, 5, 15
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")

# Интерактивный ввод
print("\n" + "=" * 50)
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

result = check_between(a, b, c)
print(f"Число B находится между числами A и C: {result}")