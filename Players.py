from Dice import *


class Joueur:
    def __init__(self):
        self.name = "Default"
        self.army = None
        self.toReplace = 0
        self.victoryPoint = 0
        self.Attack = True
        self.Replace = False
        self.lastAttack = False
        self.listCaseTemp = []

    def conquier(self, case, listeCase):
        howManyToConquier = 0
        while case.uniteOnCase > self.army > howManyToConquier:
            howManyToConquier += 1
        if howManyToConquier <= self.army:
            self.lastAttack = True
            varDice = diceRandom.randomDice()
            if self.army + varDice < case.uniteOnCase:
                print("Fail, pas assez")
                self.Attack = False
                return
        self.army.number -= howManyToConquier
        case.caseAddBeenConquiert(Joueur)
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
