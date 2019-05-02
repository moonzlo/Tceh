# Цель данного файла, обеъеднить процесс игры, и инициализировать игровое меню.

# Меню:
# - Игрок против Игрока
# - Игрок против ИИ
# - ИИ против ИИ

from main import *


class Game:
    def __init__(self, player1, player2):
        self.liters = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10
        }

        self.shot_index = {
            1: [i for i in range(12, 23)],
            2: [i for i in range(24, 35)],
            3: [i for i in range(36, 47)],
            4: [i for i in range(48, 59)],
            5: [i for i in range(60, 71)],
            6: [i for i in range(72, 83)],
            7: [i for i in range(84, 95)],
            8: [i for i in range(96, 107)],
            9: [i for i in range(108, 119)],
            10: [i for i in range(120, 132)]
        }

        # Экземпляры класса.
        self.player1 = Table(player1)
        self.player2 = Table(player2)

        # Построение стен стеки клеток.
        self.player1.table_init()
        self.player2.table_init()

        if self.player2.player_name == 'AI':
            if self.player1.player_name == 'AI':

                self.ai = AI_player(self.player2.deck)
                self.player2.auto_ships()
                self.ai_deck = self.player2.deck

                self.ai2 = AI_player(self.player1.deck)
                self.player1.auto_ships()
                self.ai_deck = self.player1.deck

            else:
                self.ai = AI_player(self.player2.deck)
                self.player2.auto_ships()
                self.ai_deck = self.player2.deck

            print('Отработал')

    def navigation(self, liter, num):
        """Возвращает индекс запрашиваемого квадрата"""

        liter_index = self.liters.get(liter.upper())

        if liter_index != None:
            index = self.shot_index.get(num)

            return index[liter_index]

        else:
            return 'Неверная буква'


    def ship_installation(self):
        """Суть данного метода, это цикл запросов на установку коробля. Сначала Игрок1 до тех пор пока не будут
        поставлены все корабли, а затем Игрок 2. Механизм работы, через бесконечный цикл"""

        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        vectors = ['left', 'right', 'up', 'down']

        for ship in ships:
            while True:  # Запускаем цикл запроса воода данных от пользователя.
                try:
                    liter = input(f'Введите БУКВУ широты, на Англйском языке, для установки {ship} палубника: ')
                    num = int(input('Введите цифру от 1 до 10, вектора долготы: '))
                    print('''
                    Выбирете вектор установки корабля: 
                    Влево  = 0
                    Вправо = 1
                    Вверх  = 2
                    Вниз   = 3
                    ''')
                    vector = int(input('Введите НОМЕР вектора по которому будет поставлен кораблик (0 - 3) : '))

                    if liter.upper() in self.liters.keys():
                        if 0 < num <= 10:
                            if 0 <= vector <= 3:
                                index = __class__.navigation(self, liter, num)

                                if index != False:

                                    my_ship = Ship(ship, index, vectors[vector],
                                                                     self.player1.deck, self.player1.deck_war)

                                    test = my_ship.auto_building()

                                    if test:
                                        print(self.player1)
                                        break
                                    else:
                                        print('Данное дейсвтие не было произведено')
                                        continue
                                else:
                                    print('Неверный индекс вектора')

                        else:
                            if num > 10:
                                print('Ваше чилсло БОЛЬШЕ!')

                            else:
                                print('Вы ввели чилсо МЕНЬШЕ!')
                    else:
                        print('Такой буквы НЕТ')

                except ValueError:
                    print('Нужно ввести ЦИФРУ!')




gamer = Game('Игрок1', 'Игрок2')

print(gamer.player2)
print(gamer.player1)
gamer.ship_installation()