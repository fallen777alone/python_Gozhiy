# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D
# (D - входной параметр целого типа, лежащий в диапазоне 0-9, K - параметр целого типа, являющийся одновременно входным и выходным). 
# С помощью этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2, выводя результат каждого добавления.

def AddRightDigit(D, K):
    # Добавляем цифру D справа к числу K
    K *= 10
    K += D
    return K

# Основной блок программы
try:
    K = int(input("Введите целое положительное число K: "))
    D1 = int(input("Введите первую цифру D1 (от 0 до 9): "))
    D2 = int(input("Введите вторую цифру D2 (от 0 до 9): "))
    
    if D1 > 9 or D1 < 0 or D2 > 9 or D1 < 0: #проверка условия
        print("Цифры должны быть в диапазоне от 0 до 9")
    
    # Последовательное добавление цифр
    K = AddRightDigit(D1, K)
    print(f"После добавления цифры {D1}, новое значение K: {K}") #добавление и вывод результата с 1 числом
    
    K = AddRightDigit(D2, K)
    print(f"После добавления цифры {D2}, новое значение K: {K}") #добавление 2 числа и вывод полноценного результата
    
except ValueError:
    print("Ошибка при вводе данных.")