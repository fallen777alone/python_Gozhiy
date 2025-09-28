#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B
#находится между числами A и C».
def check_between(a, b, c):
    if a < c:
        return a < b < c
    else:
        return c < b < a


a, b, c = 5, 10, 15
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")


a, b, c = 20, 15, 10
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")


a, b, c = 10, 5, 15
result = check_between(a, b, c)
print(f"A={a}, B={b}, C={c} -> B между A и C: {result}")


print("\n" + "=" * 50)
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

result = check_between(a, b, c)
print(f"Число B находится между числами A и C: {result}")
