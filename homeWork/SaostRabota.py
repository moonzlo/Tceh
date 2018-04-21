import random
class Trash(object):
    def __init__(self, value):
        self.value = int(value)
        self.values = []

    def trash_value(self, *trash):
        for i in trash:
            if self.value > 0:
                self.values.append(i)
                self.value -= 1
            else:
                print('Мусорка перемолнена')

    def trash_staus(self):
        allMusor = self.values
        for i in allMusor:
            print(i.name, i.zapah)
        print('Места в мусорки осталось: ', self.value)


class TrashPacet(Trash):
    def trash_staus(self):
        allMusor = self.values
        for i in allMusor:
            print(i.name, i.zapah)
        print('Места в пакете осталось: ', self.value)

    def trash_value(self, *trash):
        for i in trash:
            if self.value > 0:
                self.values.append(i)
                self.value -= 1
            else:
                print('!!! Пает с мусором перемолнен !!!')


class Musor(object):
    def __init__(self, name, zapah):
        self.name = name
        self.zapah = zapah
    def staus(self):
        print(self.name, self.zapah)


def TrashGenerator(sets):

    names = []
    for i in range(1,sets):
        names.append('Муорс{}'.format(i))
    svistvo = ['Коробка чая', 'Коробка печенья', 'Коробка сока', 'Банка кофе', 'Памперс']
    values = ['со вкусоам тыквы', 'со вкусом дерьма', 'со вкусом яблока', 'со вкусом арабики', 'со вкусом сыра']
    musor = []

    for i in range(sets):
        one = random.choice(svistvo)
        two = random.choice(values)
        musor.append(Musor(one,two))

    return musor








urna = Trash(5)
pacetik = TrashPacet(3)

test = TrashGenerator(int(2))
print(test)
urna.trash_value(*TrashGenerator(int(4)))
print(urna.trash_staus())