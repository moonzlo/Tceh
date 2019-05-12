#  Задача: настроить три уровня сложности, и два типа игры 1) ИИ против ИИ, и Игрок против ИИ
#  Уровни сложности должны включать в себя различные типы тактик, от случайной, до сбалансированной.
import random


def logger(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        print(f'Функция {func.__name__} отработала с результатом {return_value}')
        return return_value

    return wrapper


class AI_player:
    def __init__(self, war_deck):
        self.index = 0
        self.move = [
            # Тактика подразумевает наклонное движение.
            [i for i in range(13, 23, 2)],
            [i for i in range(26, 36, 2)],
            [i for i in range(38, 47, 2)],
            [i for i in range(49, 59, 2)],
            [i for i in range(63, 71, 2)],
            [i for i in range(73, 83, 2)],
            [i for i in range(86, 95, 2)],
            [i for i in range(97, 107, 2)],
            [i for i in range(110, 119, 2)],
            [i for i in range(123, 132, 2)]
        ]

        self.deck = war_deck  # Доска с кораблями противника.
        self.memory = [[]]    # Память, из списка удачных выстрелов.
        self.vector = 0
        self.error_mem = 0

    @logger
    def shot(self, shot_index):

        """Производит выстрел, если это возможно, если нет, возвращает статус клетки"""
        if hasattr(self.deck[shot_index], 'status'):  # Проверяем, есть ли клетки атрибут "статус".
            # Проверяем возможность произвести выстрел.
            status = self.deck[shot_index].status

            # Если статус клетки "пустая", производит выстрел, возвращаем False = Промах
            if self.deck[shot_index].status == 0:
                self.deck[shot_index].status = 2   # Меняем статус на "выстрел".
                self.deck[shot_index].name = '▣'   # Окрашиваем клетку.
                return False

            elif self.deck[shot_index].status == 3:  # Проверяем находиться на клетки корабль.
                shot = self.deck[shot_index].damage(shot_index)  # Записываем ответ от функции damage

                if shot == 'kill':  # При возвращении 'kill' следует что корабль был убит.
                    self.vector = 0
                    self.error_mem = 0
                    return 'kill'

                elif shot == 'boom':  # boom возвращается только в случае успешного попадания.
                    return True       # Возвращаем True для продолжения хода.

                else:
                    print(f'Что-то пошло не так в функции стрельбы, этого сообщения не должно было быть О_о')

            else:
                if self.deck[shot_index].status == 1:  # Случай когда пытаемся выстрелить в стенку.
                    return 'стенка'

                else:
                    if self.deck[shot_index].status == 2:
                        return 'сюда уже стрелял'

                    elif self.deck[shot_index].status == 4:
                        return 'выстрел по убитому'

                    else:
                        return 'всратая ошибка'
        else:
            if hasattr(self.deck[shot_index], 'status'):
                if self.deck[shot_index].status == 1:  # Случай когда пытаемся выстрелить в стенку.
                    return 'стенка'

                else:
                    return f'Что-то непонятное со статусом {self.deck[shot_index].status}'

            elif type(self.deck[shot_index]) == str:  # Случай попытки повторного выстрела в ту же клетку.
                return 'сюда уже стрелял'

            else:
                return f'Произашло исключение, индекс = [{shot_index}] | Состояние строки {self.deck[shot_index]}'

    @logger
    def random_shot_index(self):
        """Суть метода, дать как можно более чистый индекс для будущего выстрела."""
        while True:
            index = random.randrange(len(self.deck))

            if hasattr(self.deck[index], 'status'):
                status = self.deck[index].status
                if status != 1 and status != 2 and status != 4:
                    return index


    @logger
    def play(self):

        def valid_shot(index):

            if hasattr(self.deck[index], 'status'):
                status = self.deck[index].status
                if status != 1 and status != 2 and status != 4:
                    return True
                else:
                    return False

        vectors = [-1, +1, +12, -12]

        if bool(self.memory[-1]) == False:             # В случае если попаданий не было.
            index = self.random_shot_index()           # Получаем индекс для выстрела.
            shot = self.shot(index)

            if shot == 'kill':
                self.memory[-1] = 'KILL'
                self.memory.append([])
                self.error_mem = 0
                return True

            elif shot == True:
                self.memory[-1].append(index)
                return True

            else:
                return False

        elif len(self.memory[-1]) == 1:
            shot_index = self.memory[-1][0] + vectors[self.vector]
            validator = valid_shot(shot_index)           # Проверяем доступность выстрела.

            print(shot_index)
            print(self.vector)
            if validator:
                shot = __class__.shot(self, shot_index)  # Производим выстрел.

                if shot == 'kill':
                    self.memory[-1] = 'KILL'
                    self.memory.append([])
                    self.error_mem = 0
                    return True

                elif shot == True:
                    self.memory[-1].append(shot_index)
                    return True

                elif shot == False:
                    return False

            else:
                print('Выстрел невозможен, валидатор вернул False')
                """Всегда возвращаем True поскольку данных ход является ошибочным, и не затрачивает действие."""

                if len(self.memory[-1]) > 2:   # Если выстрелов было больше одного, значит вектор был верным.
                    # Инверсионный вектор направления.

                    if self.vector == 0:    # -1
                        self.vector = 1
                        self.memory[-1][-1] = self.memory[-1][0]
                        return True

                    elif self.vector == 1:  # +1
                        self.vector = 0
                        self.memory[-1][-1] = self.memory[-1][0]
                        return True

                    elif self.vector == 2:  # +12
                        self.vector = 3
                        self.memory[-1][-1] = self.memory[-1][0]
                        return True

                    elif self.vector == 3:  # -12
                        self.vector = 2
                        self.memory[-1][-1] = self.memory[-1][0]
                        return True


                else:  # Если второй выстрел производиться в неподходящую клетку, меняем вектор.
                    if self.vector != 3:
                        self.vector += 1
                        return True
                    elif self.vector > 2:
                        self.vector = 0
                        return True

                    else:
                        return f'что-то пошло не так в исключении, вектор = {self.vector}, ' \
                            f'\nсостояние память {self.memory[-1]}'

        elif len(self.memory[-1]) > 1:
            shot_index = self.memory[-1][-1] + vectors[self.vector]
            validator = valid_shot(shot_index)  # Проверяем доступность выстрела.
            if validator:
                shot = __class__.shot(self, shot_index)  # Производим выстрел.

                if shot == 'kill':  # Если выстрел был удачным.
                    self.memory[-1] = 'KILL'
                    self.memory.append([])
                    self.error_mem = 0
                    return True


                elif shot == True:
                    self.memory[-1].append(shot_index)
                    return True

                elif shot == False:
                    if self.vector == 0:    # -1
                        self.vector = 1
                        self.memory[-1][-1] = self.memory[-1][0]
                        return False

                    elif self.vector == 1:  # +1
                        self.vector = 0
                        self.memory[-1][-1] = self.memory[-1][0]
                        return False

                    elif self.vector == 2:  # +12
                        self.vector = 3
                        self.memory[-1][-1] = self.memory[-1][0]
                        return False

                    elif self.vector == 3:  # -12
                        self.vector = 2
                        self.memory[-1][-1] = self.memory[-1][0]
                        return False


                else:
                    return f'Ошибка на втором индекс памяти. Индекс выстрела = {shot_index},' \
                        f' \nВалидатор вернул {validator}'

            else:

                print(f'Выстрел невозможен, валидатор вернул False, в памяти {self.memory}, вектор {self.vector}')
                if len(self.memory[-1]) > 1:  # Если выстрелов было больше одного, значит вектор был верным.
                    if self.error_mem < 5:
                        print('Работает <----------')
                        # Инверсиурем вектор направления.

                        if self.vector == 0:  # -1
                            self.vector = 1
                            self.memory[-1][-1] = self.memory[-1][0]
                            self.error_mem += 1
                            return True

                        elif self.vector == 1:  # +1
                            self.vector = 0
                            self.memory[-1][-1] = self.memory[-1][0]
                            self.error_mem += 1
                            return True

                        elif self.vector == 2:  # +12
                            self.vector = 3
                            self.memory[-1][-1] = self.memory[-1][0]
                            self.error_mem += 1
                            return True

                        elif self.vector == 3:  # -12
                            self.vector = 2
                            self.memory[-1][-1] = self.memory[-1][0]
                            self.error_mem += 1
                            return True
                    else:
                        print('Память ошибок переполнена, делаем сброс к первому индексу.')
                        self.memory[-1][-1] = self.memory[-1][0]

                else:  # Если второй выстрел производиться в неподходящую клетку, меняем вектор.
                    print('Я опят ТУТ >_<')
                    if self.vector != 3:
                        self.vector += 1
                        return True
                    elif self.vector > 2:
                        self.vector = 0
                        return True

                    else:
                        return f'что-то пошло не так в исключении, вектор = {self.vector}, ' \
                            f'\nсостоятие память {self.memory[-1]}'
        else:
            return 'Что-то очень странное'


class Ai_normal(AI_player):
    '''Переопределяем метод случайно стрельбы на тактику.'''

    @logger
    def random_shot_index(self):
        """Суть метода, дать как можно более чистый индекс для будущего выстрела."""

        print('Работает новый')

        @logger
        def tactics_shot():
            index = 0  # Указывает на текущий индекс стрельбы.
            if len(self.move) > 1:

                if len(self.move[index]) > 1:
                    return self.move[index].pop(0)

                elif len(self.move[index]) == 1:
                    value = self.move[index].pop(0)
                    del self.move[index]
                    return value

                else:
                    return True
            else:
                return False

        while True:

            shot = tactics_shot()
            print(shot)
            if shot:
                if hasattr(self.deck[shot], 'status'):
                    status = self.deck[shot].status
                    if status != 1 and status != 2 and status != 4:
                        return shot

            else:
                index = random.randrange(len(self.deck))

                if hasattr(self.deck[index], 'status'):
                    status = self.deck[index].status
                    if status != 1 and status != 2 and status != 4:
                        return index
