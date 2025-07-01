#Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получить зарплату", а классы-наследники будут иметь свои уникальные методы
# и свойства такие как "управлять командой" и "проектировть системы".
class Worker:
    def __init__(self, name, doljnost, salary):
        self.name = name
        self.doljnost = doljnost
        self.salary = salary

    def work(self):
        print(f"{self.name} выполняет свою работу")

    def getawage(self):
        print(f"{self.name} получил зарплату в размере {self.salary} рублей")


class Manager(Worker):
    def __init__(self, name, salary):
        super().__init__(name, "Менеджер", salary)

    def manage_team(self):
        print(f"{self.name} управляет своей командой")


class Engineer(Worker):
    def __init__(self, name, salary):
        super().__init__(name, "Инженер", salary)

    def design_systems(self):
        print(f"{self.name} проектирует системы")


менеджер = Manager("Иван", 100000)
менеджер.work()
менеджер.getawage()
менеджер.manage_team()

инженер = Engineer("Петр", 80000)
инженер.work()
инженер.getawage()
инженер.design_systems()
