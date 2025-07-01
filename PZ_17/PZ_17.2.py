import tkinter as tk

def calculate(n):
    """Выполняет арифметическое действие над числами A и B и выводит результат."""

    # Получение значений из полей ввода
    a = float(a_entry.get())
    b = float(b_entry.get())

    # Выполнение соответствующего действия в зависимости от значения n
    if n == 1:
        result = a + b
    elif n == 2:
        result = a - b
    elif n == 3:
        result = a * b
    elif n == 4:
        if b != 0:
            result = a / b
        else:
            result = "Деление на ноль невозможно"
    else:
        result = "Неверный номер действия"

    # Вывод результата
    result_label["text"] = f"Результат: {result}"

# Создание главного окна
window = tk.Tk()
window.title("Арифметические действия")
window.geometry("400x200")

# Создание полей ввода
a_label = tk.Label(text="Число A:", font=("Arial", 14))
a_entry = tk.Entry(font=("Arial", 14))

b_label = tk.Label(text="Число B:", font=("Arial", 14))
b_entry = tk.Entry(font=("Arial", 14))

# Создание кнопок для выбора действия
n_buttons = []
actions = ["Сложение", "Вычитание", "Умножение", "Деление"]
for i, action in enumerate(actions):
    button = tk.Button(text=action, command=lambda n=i+1: calculate(n), font=("Arial", 14))
    button.grid(row=i, column=0)
    n_buttons.append(button)

# Создание метки для вывода результата
result_label = tk.Label(text="Результат:", font=("Arial", 14))

# Размещение элементов на окне
a_label.grid(row=0, column=1)
a_entry.grid(row=0, column=2)

b_label.grid(row=1, column=1)
b_entry.grid(row=1, column=2)

result_label.grid(row=2, columnspan=10)

# Запуск главного цикла окна
window.mainloop()