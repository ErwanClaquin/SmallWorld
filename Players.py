import Dice


class Joueur:
    def __init__(self):
        self.name = "Default"
        self.army = None

    def setName(self, name):
        self.name = name

    def addArmy(self, army):
        self.army = army

    def conquier(self, case):
        howManyToConquier = 0
        while case.uniteOnCase > self.army and howManyToConquier < self.army:
            howManyToConquier += 1
        if howManyToConquier == self.army:
            varDice = Dice.diceRandom.randomDice()
            if self.army + varDice < case.uniteOnCase:
                print("Fail, pas assez")
                return
        self.army -= howManyToConquier
        case.caseAddBeenConquiert(Joueur)
        return
