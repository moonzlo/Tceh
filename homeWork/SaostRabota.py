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



urna = Trash(5)
pacetik = TrashPacet(3)

trash = Musor('Куоск питцы', 'пахнит грибами и сыром')
trash2 = Musor('Памперс', 'пахникт очень мерзко')
trash3 = Musor('Гнилая рыба', 'амерзительная вонь')
trash4 = Musor('Пачка сока', 'пахнет яблочным соком')


urna.trash_value(trash, trash2, trash3, trash4)
pacetik.trash_value(trash2, trash4, trash3)

urna.trash_staus()
pacetik.trash_staus()
pacetik.trash_value(trash)
