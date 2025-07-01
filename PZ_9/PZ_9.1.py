#Дана строка '2020год-16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние температуры по месяцам в году.
# Преобразовать информацию из строки в словарь, найти среднюю и минимальные
# температуры, результаты вывести на экран.
temperature_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
temperatures = list(map(int, temperature_string.split()[1:]))
temperature_dict = {
    'январь': temperatures[0],
    'февраль': temperatures[1],
    'март': temperatures[2],
    'апрель': temperatures[3],
    'май': temperatures[4],
    'июнь': temperatures[5],
    'июль': temperatures[6],
    'август': temperatures[7],
    'сентябрь': temperatures[8],
    'октябрь': temperatures[9],
    'ноябрь': temperatures[10],
    'декабрь': temperatures[11]
}
sr_temperature = sum(temperatures) / len(temperatures)
min_temperature = min(temperatures)
print("Средняя температура:", sr_temperature)
print("Минимальная температура:", min_temperature)