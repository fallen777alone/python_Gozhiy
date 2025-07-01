# 2. Составить генератор (yield), который преобразует все буквенные символы в
# строчные.

def lowercase_generator(text):
    for char in text:
        yield char.lower() if char.isalpha() else char

input_text = "Hello World!"
result = ''.join(lowercase_generator(input_text))
print(result)
