class Ship():
    def __init__(self, type, start, vector, deck, dekc_war):
        self.status = 3           # Для понимания что это корабль.
        self.health = type        # Тип корабля, он же его здоровье.
        self.start_index = start  # Стартовый индекс позиции корабля.
        self.deck = deck          # Экземпляр доски окраски границ.
        self.type = type          # Для последующий итерации.
        self.vector = vector      # Направление корабля.
        self.deck_war = dekc_war  # Доска для отметки выстрелов.


    def auto_building(self):
        '''Данный метод украден из функции авто расстановки кораблей, и позволяет проверить возможность постройки
        корабля, в случае возможности, выполнить заполнение клеток.'''
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
                    # проходим в цикле по длине корабля, +1 что бы замкнуть контур допустимого.
                    valid_num = 0
                    nums = start_point
                    for _ in range(ship):  # в ship должны попадать КЛЮЧИ (то есть сами значения количества клеток)
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в противном случае возвращаем False и ищем другую точку и вектор.
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
                    # Проверят, не занята ли последняя клетка и её соседи.
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
                        # Ожидаем получить True, в противном случае возвращаем False и ищем другую точку и вектор.
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
                    # Проверят, не занята ли последняя клетка и её соседи.
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
                else:
                    print(f'Данный ход недоступен')
                    return False

            elif vector == 'left':
                if start_index:
                    valid_num = 0
                    nums = start_point

                    for _ in range(ship):
                        next_index = nums  # Первое движение вверх.
                        # Ожидаем получить True, в противном случае возвращаем False и ищем другую точку и вектор.
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

                    # Проверят, не занята ли последняя клетка и её соседи.
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
                        # Ожидаем получить True, в противном случае возвращаем False и ищем другую точку и вектор.
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
                    # Проверят, не занята ли последняя клетка и её соседи.
                    if ship_check(valid) and ship_check(valid + 12) and ship_check(valid - 12):
                        if ship_check(valid_start) and ship_check(valid_start + 12) and ship_check(
                                valid_start - 12):
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

        test = ship_point(self.vector, self.start_index, self.type, self.deck, self.deck_war)

        return test


    def kill(self):
        def validtor(index):
            if self.deck[index].status != 1:
                return True
            else:
                return False

        start = self.start_index

        if self.vector == 'up':
            for i in range(
                    self.type + 1):  # Берем на один больше для того что бы старт учитывал три клетки ПОД стартовой.

                    if i == 0:  # Три клетки ПОД основной
                        left = start +12 - 1
                        right = start + 12 + 1
                        if validtor(start + 12):
                            self.deck[start + 12].status = 4
                            self.deck[start + 12].name = '▣'

                            self.deck_war[start + 12].name = '▣'

                        if validtor(left):
                            self.deck[left].status = 4
                            self.deck[left].name = '▣'

                            self.deck_war[left].name = '▣'

                        if validtor(right):
                            self.deck[right].status = 4
                            self.deck[right].name = '▣'

                            self.deck_war[right].name = '▣'



                        # Первая клетка корабля.
                        left = start + 1
                        right = start - 1
                        if validtor(left):
                            self.deck[left].status = 4
                            self.deck[left].name = '▣'

                            self.deck_war[left].name = '▣'
                        if validtor(right):
                            self.deck[right].status = 4
                            self.deck[right].name = '▣'

                            self.deck_war[right].name = '▣'

                        start -= 12

                    elif i == self.type:  # Движение на одну клетку вверх над последней.

                        left = start - 1
                        right = start + 1
                        if validtor(start):
                            self.deck[start].status = 4
                            self.deck[start].name = '▣'

                            self.deck_war[start].name = '▣'
                        if validtor(left):
                            self.deck[left].status = 4
                            self.deck[left].name = '▣'

                            self.deck_war[left].name = '▣'
                        if validtor(right):
                            self.deck[right].status = 4
                            self.deck[right].name = '▣'

                            self.deck_war[right].name = '▣'

                    else:
                        left = start - 1
                        right = start + 1
                        if validtor(left):
                            self.deck[left].status = 4
                            self.deck[left].name = '▣'

                            self.deck_war[left].name = '▣'
                        if validtor(right):
                            self.deck[right].status = 4
                            self.deck[right].name = '▣'

                            self.deck_war[right].name = '▣'
                        start -= 12

        elif self.vector == 'down':
            for i in range(
                    self.type + 1):  # Берем на один больше для того что бы старт учитывал три клетки НАД стартовой.

                if i == 0:  # Три клетки ПОД основной
                    left = start - 12 - 1
                    right = start - 12 + 1
                    if validtor(start - 12):
                        self.deck[start - 12].status = 4
                        self.deck[start - 12].name = '▣'

                        self.deck_war[start - 12].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    # Первая клетка корабля.
                    left = start + 1
                    right = start - 1
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'

                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    start += 12

                elif i == self.type:  # Движение на одну клетку вверх над последней.

                    left = start - 1
                    right = start + 1
                    if validtor(start):
                        self.deck[start].status = 4
                        self.deck[start].name = '▣'

                        self.deck_war[start].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                else:
                    left = start - 1
                    right = start + 1
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'
                    start += 12

        elif self.vector == 'right':
            for i in range(
                    self.type + 1):

                if i == 0:  # Три клетки перед
                    left = start - 1 - 12
                    right = start - 1 + 12
                    if validtor(start - 1):
                        self.deck[start - 1].status = 4
                        self.deck[start - 1].name = '▣'

                        self.deck_war[start - 1].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    # Первая клетка корабля.
                    left = start + 12
                    right = start - 12
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    start += 1

                elif i == self.type:

                    left = start - 12
                    right = start + 12
                    if validtor(start):
                        self.deck[start].status = 4
                        self.deck[start].name = '▣'

                        self.deck_war[start].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                else:
                    left = start - 12
                    right = start + 12
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'
                    start += 1


        elif self.vector == 'left':
            for i in range(
                    self.type + 1):

                if i == 0:  # Три клетки перед
                    left = start + 1 - 12
                    right = start + 1 + 12
                    if validtor(start + 1):
                        self.deck[start + 1].status = 4
                        self.deck[start + 1].name = '▣'

                        self.deck_war[start + 1].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    # Первая клетка корабля.
                    left = start + 12
                    right = start - 12
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                    start -= 1

                elif i == self.type:

                    left = start - 12
                    right = start + 12
                    if validtor(start):
                        self.deck[start].status = 4
                        self.deck[start].name = '▣'

                        self.deck_war[start].name = '▣'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'

                else:
                    left = start - 12
                    right = start + 12
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '▣'

                        self.deck_war[left].name = '▣'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '▣'

                        self.deck_war[right].name = '▣'
                    start -= 1

    def damage(self, index):
        self.deck[index] = '▥'

        if self.health == 1:
            self.health -= 1
            self.status = 4
            __class__.kill(self)
            return 'kill'

        else:
            self.health -= 1
            return 'boom'



    def __repr__(self):
        if self.health > 0:
            return '▤'
        else:
            return '▦'