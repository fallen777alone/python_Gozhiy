# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать

def sum_range(n, m):
    total_sum = 0
    for i in range(n, m):
        total_sum += i
    return total_sum

# Основной блок программы
try:
    n = int(input("Введите начальное число n: "))
    m = int(input("Введите конечное число m: "))
    result = sum_range(n, m)
    if n > m:
        print("Ошибка! Начальное число должно быть меньше конечного.")
    else:
        print(f"Сумма чисел от {n} до {m}: {result}")
except ValueError:
    print("Ошибка! Введены некорректные данные.")