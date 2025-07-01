#В соответствии с номером варианта перейти по ссылке на прототип.
#Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу

import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Sign up")
window.geometry("500x500")


# Верхняя часть: оранжевый фон с надписью "Регистрация"

top_frame = tk.Frame(window, bg="#FF8C00", height=100)
# расположение в окне пак (фрейм будет растягиваться по горизонатли занимать всю родительскую ширину)
top_frame.pack(fill=tk.X)

tk.Label(top_frame, text="Sign Up", font=("Arial", 20, "bold"), bg="#FF8C00", fg="#ffe134").pack(side=tk.LEFT)
# Центральная часть: темно-серый фон с полями ввода
center_frame = tk.Frame(window, bg="#222536")
# если значение тру виджет будет занимать всю область контейнера
center_frame.pack(fill=tk.BOTH, expand=True)



# Поля ввода
tk.Label(center_frame, text="First name:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=0, column=0, pady=[30, 5], padx=[180, 0])
tk.Entry(center_frame, width=35).grid(row=0, column=1, pady=[30, 5])

tk.Label(center_frame, text="Last name:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=1, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=1, column=1, pady=5)

tk.Label(center_frame, text="Screen Name:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=2, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=2, column=1, pady=5)


# Выпадающие списки для даты рождения
tk.Label(center_frame, text="Date of Brith:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=3, column=0, padx=[100, 0])

# Здесь объявление переменных в которых лежат все возможные варианты выпадющих списков
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
days = [str(i) for i in range(1, 32)]
years = [str(i) for i in range(1900, 2023)]
country = ["USA", "Бельгия", "Бразилия", "Нигерия"]

# Здесь объявление переменных в которых лежат ТОЛЬКО ВЫБРАННЫЕ ЗНАЧЕНИЯ в выпадающих списках. По дефолту будет стоять первый элемент списка
month_var = tk.StringVar(center_frame, value=months[0])
day_var = tk.StringVar(center_frame, value=days[0])
year_var = tk.StringVar(center_frame, value=years[0])
country_var = tk.StringVar(center_frame, value=country[0])

tk.OptionMenu(center_frame, month_var, *months).grid(row=3, column=1, sticky=tk.W, pady=5)

tk.OptionMenu(center_frame, day_var, *days).grid(row=3, column=1, sticky=tk.W, pady=5, padx=[90, 0])

tk.OptionMenu(center_frame, year_var, *years).grid(row=3, column=1, sticky=tk.W, pady=5, padx=[150, 0])


# Поле "Пол" с радиокнопками
tk.Label(center_frame, text="Gender:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=4, column=0, padx=[180, 0])

# Создание переменной для хранения выбранного пола. Изначально она не имеет значения.
gender_var = tk.IntVar()
# Создание радиокнопок
tk.Radiobutton(center_frame, text="Mate", variable=gender_var, value=1).grid(row=4, column=1, sticky=tk.W, pady=5)
tk.Radiobutton(center_frame, text="Female", variable=gender_var, value=2).grid(row=4, column=1, sticky=tk.W, pady=5, padx=[85, 0])


#Страна(выпадающий)
tk.Label(center_frame, text="Country:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=5, column=0, padx=[160, 0])
# country_option_menu = tk.OptionMenu(center_frame, country_var, country)
# country_option_menu.config(width=15)
# country_option_menu.grid(row=5, column=1, pady=5, sticky=tk.W)
tk.OptionMenu(center_frame, country_var, *country).grid(row=5, column=1,pady=5, sticky=tk.W)




# Поля ввода для email, телефона, пароля и подтверждения пароля
tk.Label(center_frame, text="E-mail:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=6, column=0, padx=[170, 0])
tk.Entry(center_frame, width=35).grid(row=6, column=1, pady=5)

tk.Label(center_frame, text="Phone:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=7, column=0, padx=[150, 0])
tk.Entry(center_frame, width=35).grid(row=7, column=1, pady=5)

tk.Label(center_frame, text="Password:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=8, column=0, padx=[160, 0])
tk.Entry(center_frame, width=35, show="*").grid(row=8, column=1, pady=5)

tk.Label(center_frame, text="Confirm Password:", font=("Arial", 12), bg="#222536", fg="#ffe134").grid(row=9, column=0, padx=[40, 0])
tk.Entry(center_frame, width=35, show="*").grid(row=9, column=1, pady=5)



# Чекбокс и надпись
# Создание переменной для хранения текущего значения чекбокса. Изначально она не имеет значения.
terms_var = tk.IntVar()
tk.Checkbutton(center_frame, text="I agree to the Terms of Use", variable=terms_var, fg="#ffe134", selectcolor="#222536", bg="#222536" ).grid(row=11, columnspan=2, padx=[150, 0])


# Нижняя строка: оранжевый фон с кнопками
bottom_frame = tk.Frame(window, bg="#FF8C00", height=400)
bottom_frame.pack(fill=tk.X)

cancel_button = tk.Button(bottom_frame, text="Cancel", bg="red", fg="white")
# tk.Right - расположен с правой стороны фрейма
cancel_button.pack(side=tk.RIGHT, padx=10)
# Создаем зеленую кнопку регистрации
register_button = tk.Button(bottom_frame, text="Submit", bg="green", fg="white")
register_button.pack(side=tk.RIGHT, padx=10)


window.mainloop()