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
'''

class Notes(object):
    def __init__(self):
        self.sets = 0
        self.notes = []

    def adder(self, text):
        self.sets += 1
        self.notes.append('{}:{}'.format(self.sets,text))

    def printer(self):
        for i in self.notes:
            print(i)




ab = Notes()
ab.adder('2заметка')
ab.adder('3заметка')
ab.adder('4заметка')
ab.printer()
