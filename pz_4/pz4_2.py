# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на Р процентов от пробега предыдущего дня (Р — вещественное, 0 < Р < 50).
# По данному Р определить, после какого дня суммарный пробег лыжника за все дни превысит 200 км
# и вывести найденное количество дней К (целое) и суммарный пробег S (вещественное число).

# Алгоритм функции:
# Сначала устанавливается начальная дневная дистанция в 10 километров.
# Далее запускается бесконечный цикл while True, который выполняет следующие действия:
# Увеличиваем счетчик дней на единицу.
# Добавляем дневную дистанцию к общей дистанции.
# Проверяем, превысила ли общая дистанция порог в 200 километров. Если да, прерываем выполнение цикла командой break.
# Рассчитываем новую дневную дистанцию, увеличивая её на заданный процент P.
# После выхода из цикла возвращаем количество дней и общую дистанцию, округленную до двух знаков после запятой.

def calculate_days_and_distance(P): #функция, P - формальный оператор (написал на всякий если спросит)
    total_distance = 0
    daily_distance = 10
    day_count = 0

    while True:
        try:
            day_count += 1
            total_distance += daily_distance
            
            if total_distance > 200:
                break
                
            daily_distance *= (1 + P / 100)
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    return day_count, round(total_distance, 2) #на этой строчке функция заканчивается

# Ввод значения P

# Описание блока:
# Этот блок предназначен для получения от пользователя значения процента увеличения пробега. Программа проверяет, 
# находится ли введенное значение в пределах от 0 до 50. Если нет, выводится сообщение о необходимости повторного ввода.
# Конструкция try...except используется для обработки возможных ошибок, связанных с неправильным вводом данных (например, если пользователь введет строку вместо числа).
while True:
    try:
        P = float(input("Введите процент увеличения пробега (в диапазоне от 0 до 50): "))
        if 0 < P < 50:
            break
        else:
            print("Процент должен быть в диапазоне от 0 до 50. Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод. Введите число.")

K, S = calculate_days_and_distance(P) #вывод результата
print(f"После {K} дней суммарный пробег составит {S} км.")