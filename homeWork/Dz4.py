'''
*ЗАДАЧА 1:
Реализовать класс Person, у которого должно быть два публичных поля: age и name.
Также у него должен быть следующий набор методов: know(person), который позволяет
добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека

*ЗАДАЧА 2:
Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

*ЗАДАЧА 3:
Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
'''


# Task 1 | Создаем класс друзья с возможность добавлять знакомых.

class Person(object):

    def __init__(self, name):
        self.name = name
        self.frand_list = []

    def know(self, person):
        if isinstance(drug1, Person):  # Проверяем относиться ли объект к классу.
            self.frand_list.append(person)
        else:
            print('Ошибка !', person, 'НЕ являеться объектом класса Person')

    def is_know(self, person):
        for i in self.frand_list:
            if i == person:
                print('Да они друзья')
            else:
                print('Увы они пока не дружат')
        return ''



drug1 = Person('Митя')
drug2 = Person('Вася')

drug1.know(drug2)
print(drug1.is_know(drug2))

# Task 2 | Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer(object):
    def log(self, *values):
        for i in values:
            print(i)

class FormattedPrinter(Printer):
    def log(self, *values):
        for i in values:
            print(i,'\n********')

test = Printer()
test2 = FormattedPrinter()

test2.log('Строка1','Строка2','Строка3','Строка4')

# Task 3 | Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека
# (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Animal(object):
    def __init__(self, name, types):
        self.name = name
        self.types = types

class Human(object):
    def __init__(self, name):
        self.name = name

    def is_dangerous(self, animal):
        if animal.types == 'Хищник':
            return '{} опасн(а) для людей'.format(animal.name)
        elif animal.types == 'Ядовитый':
            return '{} опасн(а) для людей'.format(animal.name)
        else:
            return '{} безобидное зверьё'.format(animal.name)