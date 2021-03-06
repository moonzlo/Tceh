import random
from ship_func import Ship
from AIplayers import *

class Kletka():
    def __init__(self, x):
        self.name = '⬚'
        self.index = x
        self.status = 0  # 0 = Пустота | 1 = Стенка | 2 = Выстрел | 3 = Клетка корабля | 4 = Убитый

    def __repr__(self):
        return f'{self.name}'


class Table():
    def __init__(self, name):
        self.player_name = name

        # Создаем список из пустых экземпляров (клеток)
        self.deck = [Kletka(x) for x in range(144)]
        self.deck_war = [Kletka(x) for x in range(144)]

    def table_init(self):
        """определение границ поля достки"""
        start = 0
        for x in range(10):
            start += 11
            self.deck[start].name = '▨'
            self.deck_war[start].name = '▨'
            self.deck[start].status = 1
            start += 1
            self.deck[start].name = '▨'
            self.deck_war[start].name = '▨'
            self.deck[start].status = 1

        for x in self.deck[:11]: x.name = '▨'
        for x in self.deck_war[:11]: x.name = '▨'
        for x in self.deck[:11]: x.status = 1
        for x in self.deck[131:]: x.name = '▨'
        for x in self.deck_war[131:]: x.name = '▨'
        for x in self.deck[131:]: x.status = 1

    def auto_ships(self, deck_war):

        def ship_point(vector, start_point, ship, deck, deck_war):

            def index_validator(index):
                if deck[index].status != 0:
                    return False

                else:
                    return True

            def ship_check(index):
                if deck[index].status != 3:
                    return True
                else:
                    return False

            start_index = index_validator(start_point)

            if vector == 'up':
                if start_index:
                    # проходим в цикле по длинне коробля, +1 что бы замкнуть контур допустимного ариола.
                    valid_num = 0
                    nums = start_point
                    for _ in range(ship):  # в ship должны попадать КЛЮЧИ (то есть сами значения количества клеток)
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в пративном случае возвращаем False и ищем другую точку и вектор.
                        point = ship_check(next_index)
                        right_index = ship_check(next_index + 1)
                        lift_index = ship_check(next_index - 1)
                        valid_point = index_validator(next_index)

                        if 12 < next_index < 131:
                            if point and right_index and lift_index and valid_point:
                                valid_num += 1

                        else:
                            return False

                        nums -= 12

                    valid = start_point - ship * 12
                    # Проверят, не заняти ли последняя клетка и её соседи.
                    if ship_check(valid) and ship_check(valid + 1) and ship_check(valid - 1):
                        if ship_check(start_point + 12) and ship_check(start_point + 13) and ship_check(
                                start_point + 11):

                            if valid_num == ship:  # Проверяет, все ли клетки были пусты и пригодны для жизни =)

                                korablik = Ship(ship, start_point, vector, deck, deck_war)
                                # deck[start_point].name = '🞓'
                                # deck[start_point].status = 3
                                deck[start_point] = korablik
                                next_point = start_point
                                for i in range(ship):
                                    deck[next_point] = korablik
                                    # deck[next_point].name = '🞓'
                                    # deck[next_point].status = 3
                                    next_point -= 12

                                return True

                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

            elif vector == 'down':
                if start_index:
                    valid_num = 0
                    nums = start_point
                    for _ in range(ship):
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в пративном случае возвращаем False и ищем другую точку и вектор.
                        point = ship_check(next_index)
                        right_index = ship_check(next_index + 1)
                        lift_index = ship_check(next_index - 1)
                        valid_point = index_validator(next_index)

                        if 12 < next_index < 131:
                            if point and right_index and lift_index and valid_point:
                                valid_num += 1

                        else:

                            return False

                        nums += 12

                    valid = start_point + ship * 12
                    # Проверят, не заняти ли последняя клетка и её соседи.
                    if ship_check(valid) and ship_check(valid + 1) and ship_check(valid - 1):
                        if ship_check(start_point - 12) and ship_check(start_point - 13) and ship_check(
                                start_point - 11):

                            if valid_num == ship:  # Проверяет, все ли клетки были пусты и пригодны для жизни =)
                                korablik = Ship(ship, start_point, vector, deck, deck_war)
                                # self.deck[start_point].name = '🞓'
                                # self.deck[start_point].status = 3
                                deck[start_point] = korablik
                                next_point = start_point
                                for i in range(ship):
                                    deck[next_point] = korablik
                                    # self.deck[next_point].name = '🞓'
                                    # self.deck[next_point].status = 3
                                    next_point += 12

                                return True

                            else:

                                return False
                        else:

                            return False
                    else:

                        return False

            elif vector == 'left':
                if start_index:
                    valid_num = 0
                    nums = start_point

                    for _ in range(ship):
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в пративном случае возвращаем False и ищем другую точку и вектор.
                        point = ship_check(next_index)
                        right_index = ship_check(next_index + 12)
                        lift_index = ship_check(next_index - 12)
                        valid_point = index_validator(next_index)

                        if 12 < next_index < 131:
                            if point and right_index and lift_index and valid_point:
                                valid_num += 1
                        else:
                            return False
                        nums -= 1

                    valid = start_point - ship
                    valid_start = start_point + 1

                    # Проверят, не заняти ли последняя клетка и её соседи.
                    if ship_check(valid) and ship_check(valid + 12) and ship_check(valid - 12):
                        if ship_check(valid_start) and ship_check(valid_start + 12) and ship_check(valid_start - 12):
                            korablik = Ship(ship, start_point, vector, deck, deck_war)
                            if valid_num == ship:  # Проверяет, все ли клетки были пусты и пригодны для жизни =)
                                # deck[start_point].name = '🞓'
                                # deck[start_point].status = 3
                                deck[start_point] = korablik
                                next_point = start_point

                                for i in range(ship):
                                    deck[next_point] = korablik
                                    # deck[next_point].name = '🞓'
                                    # deck[next_point].status = 3
                                    next_point -= 1
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False

            elif vector == 'right':
                if start_index:
                    valid_num = 0
                    nums = start_point

                    for _ in range(ship):
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в пративном случае возвращаем False и ищем другую точку и вектор.
                        point = ship_check(next_index)
                        right_index = ship_check(next_index + 12)
                        lift_index = ship_check(next_index - 12)
                        valid_point = index_validator(next_index)

                        if 12 < next_index < 131:
                            if point and right_index and lift_index and valid_point:
                                valid_num += 1
                        else:
                            return False
                        nums += 1

                    valid = start_point + ship
                    valid_start = start_point - 1

                    # Проверят, не заняти ли последняя клетка и её соседи.
                    if ship_check(valid) and ship_check(valid + 12) and ship_check(valid - 12):
                        if ship_check(valid_start) and ship_check(valid_start + 12) and ship_check(valid_start - 12):
                            korablik = Ship(ship, start_point, vector, deck, deck_war)
                            if valid_num == ship:  # Проверяет, все ли клетки были пусты и пригодны для жизни =)
                                # deck[start_point].name = '🞓'
                                # deck[start_point].status = 3
                                deck[start_point] = korablik
                                next_point = start_point
                                for i in range(ship):
                                    deck[next_point] = korablik
                                    # deck[next_point].name = '🞓'
                                    # deck[next_point].status = 3
                                    next_point += 1
                                return True

                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                print('Неверный вектор')

        vectors = ['left', 'right', 'up', 'down']

        ships = {4: 1, 3: 2, 2: 3, 1: 4}

        for i in ships:
            for x in range(ships.get(i)):
                while True:
                    random_start = random.randint(13, 131)
                    vector = random.choice(vectors)
                    ship = ship_point(vector, random_start, i, self.deck, deck_war)

                    if ship == True:
                        break

                    else:
                        continue

    def __repr__(self):
        stroka = ''
        stroka += f'==============={self.player_name}==================\n'
        stroka += '   %4s%3s%2.8s%3s%2s%2s%3s%2s%3s%2s \n' % ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        num = 0
        str_num2 = 1
        stroka += '   '
        for x in self.deck:
            if num != 11:
                stroka += f'{x} '
                num += 1
            else:
                stroka += f'{x}\n'
                if str_num2 < 10:
                    stroka += f'{str_num2}  '
                    str_num2 += 1
                elif str_num2 == 10:
                    stroka += f'{str_num2} '
                    str_num2 += 1
                else:
                    stroka += f'   '

                num = 0


        stroka2 = ''
        stroka2 += '   %4s%3s%2.8s%3s%2s%2s%3s%2s%3s%2s \n' % ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        num = 0
        str_num = 1
        stroka2 += '   '
        for x in self.deck_war:
            if num != 11:
                stroka2 += f'{x} '
                num += 1
            else:
                stroka2 += f'{x}\n'
                if str_num < 10:
                    stroka2 += f'{str_num}  '
                    str_num += 1
                elif str_num == 10:
                    stroka2 += f'{str_num} '
                    str_num += 1
                else:
                    stroka2 += f'   '

                num = 0
        return f'{stroka}\n \n{stroka2}'



# player1 = Table('PLAYER 1')
# player2 = Table('PLAYER 2')
#
#
# game1 = Game(player1, player2)
# game1.game_init()
#
# deck = player1.deck
# import AIplayers
#
# test = AIplayers.AI_player(deck)
# # deck[94].status = 4
#
# test.play()
# test.play()
# test.play()
# print(player1)
#
#
# print(test.memory)