# Запихать в отдельный файл !)
# ⧈ | ☒ | ■ | □ | 🞓 | ▧ | ⬚ | 🞕 | 🞔
import random


class Kletka(object):
    def __init__(self, status=False):
        self.status = status
        self.name = self


    def get_position(self, listname):
        pos = listname.index(self.name)
        return pos

    def __repr__(self):
        if self.status == False:
            return '□'
        elif self.status == True:
            return '■'
        elif self.status == 'block':
            return '🞔'


class Deck(object):
    def __init__(self):
        self.deck = []


    def generatorDeck(self):
        while len(self.deck) != 10:
            spisok2 = []
            for i in range(10):
                spisok2.append(Kletka())
            self.deck.append(spisok2)


    def SetShip(self, typeShip, position):
        pass


    def printer(self):
        for i in self.deck:
            for x in i:
                print(x, end='')
            print('')  # для создания столбика








doska1 = Deck()
doska1.generatorDeck()

def shipSellet(decks):
    # vector Move = up    [+][0] if move >= 9
    # vector Move = down  [-][0] if move >= 0
    # vector Move = left  [0][-] if move >= 0
    # vector Move = right [0][+] if move >= 9

    while True:
        vectors = ['up', 'down', 'left', 'right']
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        vectorRandom = random.choice(vectors)

        pointX = random.randrange(10)
        pointY = random.randrange(10)
        print(pointX, pointY)

        if vectorRandom == 'up':
            if pointX - ships[0] + 1 >= 0:
                sellect = int(pointX)
                for i in range(ships[0]):
                    decks.deck[sellect][pointY].status = True
                    sellect -= 1 # рост вверх
                break


        elif vectorRandom == 'down':
            if 9 >= pointX + ships[0] - 1 >= 0:
                sellect = int(pointX)
                for i in range(ships[0]):
                    decks.deck[sellect][pointY].status = True
                    sellect += 1  # рост вниз

                break

        elif vectorRandom == 'left':
            if 9 >= pointY - ships[0] + 1 >= 0:
                sellect = int(pointY)
                for i in range(ships[0]):
                    decks.deck[pointX][sellect].status = True
                    sellect -= 1  # рост в лево
                break

        elif vectorRandom == 'rigth':
            if 9 >= pointY + ships[0] - 1 >= 0:
                sellect = int(pointY)
                for i in range(ships[0]):
                    decks.deck[pointX][sellect].status = True
                    sellect += 1  # рост в право
                break








shipSellet(doska1)
doska1.printer()