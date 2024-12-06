# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B
# находится между числами A и C».

try:
    while True:
        A = int(input("Введите целое число A: "))
        B = int(input("Введите целое число B: "))
        C = int(input("Введите целое число C: "))

        if A < 0 or B < 0 or C < 0:
            print("Числа не могут быть меньше нуля!")
            continue
        else:
            break

    if A < B < C:
        print(True)
    else:
        print(False)

except ValueError:
    print("Ошибка при вводе данных!")