'''   Задача: Создать программу Заметки !
Фкнеционал:
- Создать заметку (купить)
- Создать заметку (сделать)
- Создать заметку URL
- У кадой заметки должен быть заголовок, и тело.
- Возможность отметить задание выполненным (отменить выполнение)
- Значение Выполненного/Невыполненного задания должен отражаться в списке заданий как ( + или - )

Реализация:
- Написать логику в файле main
- Функции вынести в файл function
- Каждая заметка должна быть экземпляром класса.
'''
import os  # Для очичистки консоли
clear = lambda: os.system('cls')


class Notes(object):
    def __init__(self):
        self.notes = []

    def adder(self, obj):
        self.notes.append(obj)

    def printer(self):
        for i in self.notes:
            print('{}) {}'.format(self.notes.index(i),i.printer()))



class Not(object):
    def __init__(self, type, title, text):
        self.type = type
        self.title = title
        self.text = text
        self.ststus = False


    def statuse(self):
        if self.ststus == False:
            return '-'
        elif self.ststus == True:
            return '+'

    def printer(self):
        status = self.statuse()
        return '{}: {} : {} | Статус выполнения [{}]'.format(self.type,self.title,self.text,status)


if __name__ == '__main__':
    zametka = Notes()

    def initer():
        while True:

            print('''
            Выберите тип действий: 
            1 - Создать заметку
            2 - Удалить заметку
            3 - Отметить как сделано
            4 - Отменить выполнение
            5 - Посмотреть все заметки
            6 - Выйти
            ''')
            try:
                menu = int(input('Введите число: '))


                if menu == 1:
                    clear()
                    while True:
                        print('''
                        Выберите тип заметки которую хотите создать:
                              1 - Задание
                              2 - Заметка
                              3 - URL
                        ''')
                        vvod = int(input('Введите число: '))
                        if vvod == 1:
                            title = input('Введите название задания: ')
                            text = input('Введите текст задания: ')
                            notes = Not('Задание',title,text)
                            zametka.adder(notes)
                            clear()
                            break

                        elif vvod == 2:
                            title = input('Введите название заметки: ')
                            text = input('Введите текст зааметки: ')
                            notes = Not('Заметка',title,text)
                            zametka.adder(notes)
                            clear()
                            break

                        elif vvod == 3:
                            title = input('Введите название ссылки: ')
                            text = input('Введите URL: ')
                            notes = Not('URL',title,text)
                            zametka.adder(notes)
                            clear()
                            break

                        else:
                            clear()
                            print('Такого пункта меню нет.')

                elif menu == 2:
                    clear()
                    while True:
                        print('''
                        Удаление заметок происходит по индексу который указан Перед заметкой
                                        Вот список заметок которые у нас есть:
                        ''')
                        zametka.printer()
                        try:
                            menu2 = int(input('Введи индекс заметки которую нужно удалить: '))
                            rempves = zametka.notes[menu2]
                            actept = input('Подтвердите удаление {} | Y = да N = нет '.format(rempves.title))
                            if actept.upper() == 'Y':
                                print('Заметка: {} успешно удалена.'.format(rempves.title))
                                zametka.notes.remove(rempves)
                                break
                            else:
                                break
                        except:
                            print('Такого индекса у нас нет.')
                            break

                elif menu == 3:
                    print('Выберете какое задание отметить как Выполненное: ')
                    zametka.printer()
                    try:
                        menu2 = int(input('Введи индекс: '))
                        rempves = zametka.notes[menu2]
                        if rempves.ststus == False:
                            rempves.ststus = True
                            clear()
                            print('Отличная работа')
                        else:
                            print(rempves.title, 'уже сделано !')



                    except:
                        print('Такого индекса у нас нет.')



                elif menu == 4:
                    print('Выберете какое задание отменить: ')
                    zametka.printer()
                    try:
                        menu2 = int(input('Введи индекс: '))
                        rempves = zametka.notes[menu2]
                        if rempves.ststus == True:
                            rempves.ststus = False
                            clear()
                            print(rempves.title,'Отменили')
                        else:
                            clear()
                            print(rempves.title,'и так еще не сделано !')



                    except:
                        print('Такого индекса у нас нет.')


                elif menu == 5:
                    zametka.printer()
                    input('Нажми Enter что бы продолжить')
                    clear()
                elif menu == 6:
                    break
                else:
                    print('Такого у нас нет....')
            except Exception as error:
                print('Я же просил ЧИСЛО вот вам и ошибка...', error)
    initer()