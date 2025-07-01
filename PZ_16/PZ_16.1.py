#Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и "деление".
#Каждый метод должен принимать два аргумента и возвращать результат операции

class Calc:
    def Addition(self, a, b):
        return a + b
    def Subtraction(self, a, b):
        return a - b

    def Multiplication(self, a, b):
        return a * b
    def Division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('Деление на 0 невозможно')
            exit()

Calculate = Calc()
a = 5
b = 5
result = Calculate.Addition(a, b)
print("Сложение", result)
result = Calculate.Subtraction(a, b)
print("Вычитание", result)
result = Calculate.Multiplication(a, b)
print("Умножение", result)
result = Calculate.Division(a, b)
print("Деление", result)
