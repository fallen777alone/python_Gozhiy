#2. Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка 'ln PyCharm, you can third-party standalone applications and run them as External Tools'
import string
stroka = 'ln PyCharm, you can third-party standalone applications and run them as External Tools'
print(stroka)
lowercase_characters = list(filter(lambda x: x in string.ascii_lowercase, stroka))
result = ''.join(lowercase_characters)
print('Cимволы только нижнего регистра:', result)