from Dice import *


class Joueur:
    def __init__(self):
        self.name = "Default"
        self.army = None
        self.toReplace = 0
        self.victoryPoint = 5
        self.Attack = True
        self.Replace = False
        self.lastAttack = False
        self.listCaseTemp = []

    def conquier(self, case):
        howManyToConquier = 0
        while case.NumberuniteOnCase > howManyToConquier <self.army.number:
            howManyToConquier += 1
        print(howManyToConquier)
        if howManyToConquier < case.NumberuniteOnCase:
            return case
        """self.lastAttack = True
            varDice = diceRandom.randomDice()
            if self.army.number + varDice < case.NumberuniteOnCase:
                print("Fail, pas assez")
                self.Attack = False
                return"""
        self.army.number -= howManyToConquier
        print(self.army.number)
        case.caseAddBeenConquiert(self, howManyToConquier)
        return case

    def stack(self, listeCase):
        for cases in listeCase:
            if cases.typeOfUniteOnCase == self.army.race:
                listeCase.remove(cases)
                cases.NumberuniteOnCase = 1
                self.toReplace += cases.NumberuniteOnCase - 1
                listeCase.append(cases)
        return listeCase

    def replaceArmy(self, case):
        if case.typeOfUniteOnCase == self.army.race:
            case.NumberuniteOnCase += 1
            self.toReplace -= 1
            return case
