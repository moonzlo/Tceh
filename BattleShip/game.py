# Цель данного файла, обеъеднить процесс игры, и инициализировать игровое меню.
import time

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
                print(self.player1)
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

        print('ПЕРВЫЙ ИГРОК ЗАКОНЧИЛ РАССТАНОВКУ, ПРИШЛА ПОРА ИГРОКА 2')

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
                                                                     self.player2.deck, self.player2.deck_war)

                                    test = my_ship.auto_building()

                                    if test:
                                        print(self.player2)
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

    def menu(self):
        """Запуспк цикла самой игры, от предложения выбора с кем играть, до результатов победы."""

        print('''
        Добро пожаловать в игру Морской бой (ревизия от 03.05.2019) by moonz
        
        Данный проект очень важен для меня, потому что он стал некой точкой перехода от простого любопытства, 
        до серьезного изучения программирования. Эту версию я делаю спустя целый ГОД с момента первой попытки, 
        которая сильно демотивироваламеня своей сложность. Дело в том что данная задача была в рамках курса который 
        я проходил, и я не мог себе позволить продолжить обучение не решив это дз. По этому почти год я ничего не 
        писал вообще, а потом вернулся с другой стороны. Я уже в совершенстве могу писать прасеры, ботов на селениум, 
        но вот данный орешек был для меня неподъемным. Сейчас же я имею опыт уже серьезного проекта по автоматизации, 
        и хоть алгоритмов и паттернов проектирования я всё ещё не знаю, это не помешало меня потратить две недели на 
        написание логики этой игры.
        
        ''')



def battle(game_set):
    print(f'Начёнм игру. Первым ходит {game_set.player1.player_name}')
    input('Нажми Enter для продолжения')

    def shot(player):
        try:
            print(f'Сейчас стреляет игрок {player.player_name}')
            print('Куда будем стрелять? ')
            vector = input('Введите английскую букву от A до J: ')
            num = int(input('Введите номер оси Y: '))

            shot_index = game_set.navigation(vector, num)

            return shot_index

        except ValueError:
            print('Вы ввели НЕ ЧИСЛО')
            return True


    while True:  # Цикл игры
        index = 0
        players = [game_set.player1, game_set.player2]

        if index == 0:   # Стрелят игрок 1 в игрока 2
            shot_index = shot(players[index])
            deck = game_set.player2.deck
            if deck[shot_index].status == 3:
                deck[shot_index].name = '▣'
                deck[shot_index].status = 2

                fire = deck[shot_index].damage(shot_index)

                print(game_set.player2)
            elif deck[shot_index].status == 0:
                print('Промазал =(')
                deck[shot_index].name = '▣'
                deck[shot_index].status = 2


        elif index == 1:  # Стрелят игрок 2 в игрока 1
            shot_index = shot(players[index])
            deck = game_set.player1.deck

        else:
            print('Ошибка индекса')


while True:  # Цикл основного меню.
    print('''
    Основное меню игры:
    
    1 - Играть против друга (Player1 & Player2)
    
    2 - Играть против ИИ (Player1 & AiPlayer)
    
    3 - Смотреть за игрой ИИ против ИИ 
    ''')
    try:
        menu_scelect = int(input('Введи номер пункта меню: '))
        if 0 < menu_scelect <= 3:

            if menu_scelect == 1:    # Игрок против Игрока
                player_name1 = input('Введите имя для первого игрока: ')
                player_name2 = input('Введите имя для второго игрока: ')

                game_set = Game(player_name1, player_name2)

                print('''
                Выбирете способ расстановки кораблей: 
                
                1 - Ручная установка каждого корабля.
                2 - Автоматичиская расстановка.
                ''')

                mode = int(input('Введите ЧИСЛО: '))
                if 0 < mode <= 2:

                    if mode == 1:  # Ручная расстановка + цикл игры

                        game_set.ship_installation()
                        print(battle(game_set))
                        break

                    else:          # Автоматичиская расстановка + цикл игры
                        p1 = game_set.player1
                        p1.auto_ships()
                        p2 = game_set.player2
                        p2.auto_ships()

                        print(game_set.player1)
                        print(game_set.player2)

                        print(battle(game_set))
                        pass

                else:
                    print('Такого пункта небыло!')
                    time.sleep(1)


            elif menu_scelect == 2:  # Игрок против ИИ
                pass

            elif menu_scelect == 3:   # ИИ против ИИ
                pass



        else:
            print('Такого пункта меню нет =(')
            time.sleep(1)

    except ValueError:
        print('Вводить нужно только ЧИСЛО!!!')
        time.sleep(2)



