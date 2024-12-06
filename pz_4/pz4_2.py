def calculate_days_and_distance(P):
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

    return day_count, round(total_distance, 2)

# Ввод значения P
while True:
    try:
        P = float(input("Введите процент увеличения пробега (в диапазоне от 0 до 50): "))
        if 0 < P < 50:
            break
        else:
            print("Процент должен быть в диапазоне от 0 до 50. Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод. Введите число.")

K, S = calculate_days_and_distance(P)
print(f"После {K} дней суммарный пробег составит {S} км.")