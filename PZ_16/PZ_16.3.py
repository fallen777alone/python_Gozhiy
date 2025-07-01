# Для задачи из блока 1 создать две функции, save_def и load_def,
# которые позволяют сохранять информацию из экземпляров класса (3шт) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации обьектов Python в бинарном формате
import pickle
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

def save_def(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
save_def(Calculate, 'calc_obj.pkl')

# Загрузка объектов из файла
Calc_new = load_def('calc_obj.pkl')

result = Calc_new.Addition(a, b)
print("Сложение", result)
result = Calc_new.Subtraction(a, b)
print("Вычитание", result)
result = Calc_new.Multiplication(a, b)
print("Умножение", result)
result = Calc_new.Division(a, b)
print("Деление", result)