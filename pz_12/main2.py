# Составить генератор (yield), который преобразует все буквенные символы в
# строчные.

def lowercase_generator(input_sequence):
    for char in input_sequence:
        if isinstance(char, str) and char.isalpha():
            yield char.lower()
        else:
            yield char

# Пример использования
input_string = input('Введите строку: ')
print("Исходная строка:", input_string)

# Создаем генератор
gen = lowercase_generator(input_string)

# Преобразованная строка
result = ''.join(gen)
print("Результат:", result)