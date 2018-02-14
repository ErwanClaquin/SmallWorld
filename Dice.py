import random

class Dice:
    def __init__(self):
        self.dice = (0,0,1,1,2,3)

    def randomDice(self):
        return self.dice[random.randint(0, 6)]


diceRandom = Dice()