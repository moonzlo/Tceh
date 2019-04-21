class Ship():
    def __init__(self, type, start, vector, deck):
        self.status = 3           # Для понимания что это корабль.
        self.health = type        # Тип коробля, он же его здоровье.
        self.start_index = start  # Стартовый индекс позиции коробля.


        self.deck = deck          # Экземпляр доски окраски границ.
        self.type = type          # Для последующий итерации.
        self.vector = vector      # Направление коробля.

    def kill(self):
        def validtor(index):
            if self.deck[index].status != 1:
                return True
            else:
                return False


        start = self.start_index
        for i in range(self.type + 1):  # Берем на один больше для того что бы старт учитывал три клетки ПОД стартовой.

                if i == 0:  # Три клетки ПОД основной
                    left = start +12 - 1
                    right = start + 12 + 1
                    if validtor(start + 12):
                        self.deck[start + 12].status = 4
                        self.deck[start + 12].name = '🞕'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '🞕'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '🞕'

                    # Первая клетка корабля.
                    left = start + 1
                    right = start - 1
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '🞕'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '🞕'

                    start -= 12

                elif i == self.type:  # Движение на одну клетку вверх над последней.

                    left = start - 1
                    right = start + 1
                    if validtor(start):
                        self.deck[start].status = 4
                        self.deck[start].name = '🞕'
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '🞕'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '🞕'

                else:
                    left = start - 1
                    right = start + 1
                    if validtor(left):
                        self.deck[left].status = 4
                        self.deck[left].name = '🞕'
                    if validtor(right):
                        self.deck[right].status = 4
                        self.deck[right].name = '🞕'
                    start -= 12

    def damage(self, index):
        self.deck[index] = '⊞'
        if self.health == 1:
            self.health -= 1
            self.status = 4
            __class__.kill(self)
            return True
        else:
            self.health -= 1
            return 'boom'



    def __repr__(self):
        if self.health > 0:
            return '🞓'
        else:
            return '⊞'