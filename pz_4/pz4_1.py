#Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A
#до B включительно.

# Основной блок программы
try:
    A = int(input("Введите целое число A: "))
    B = int(input("Введите целое число B: "))
    result = 1

    if A >= B: #проверка условия A < B
        print("Ошибка: A должно быть меньше B.")
    else:
        for i in range(A, B): #если доебется до +1, то скажи что без него выведет неверный ответ. тип если без +1, то у тя на 1 десяток меньше выведет
             #если продолжит доебывать, то кабину ей снеси
            result *= i

    print(f"Произведение всех целых чисел от {A} до {B}:", result) #ес че, f перед кавычками позволяет выводить переменные так, как тут написано, а не стандартное print("пр", A)
    #(A - переменная)
except ValueError:
    print("Произошла ошибка при вводе данных")