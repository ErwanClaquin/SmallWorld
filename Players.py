from Dice import *


class Joueur:
    def __init__(self):
        self.name = "Default"
        self.army = None
        self.victoryPoint = 5
        self.Attack = True
        self.lastAttack = False
        self.listCaseTemp = []

    def conquier(self, case, listeCase):
        canConquierAdjacent = True
        canConquierMer = True
        canConquier = True

        for casees in listeCase:
            if casees.typeOfUniteOnCase == self.army.race:
                canConquierMer = False
                #print("Il y'a des unités sur le plateau")

        if canConquierMer is False:  # Il y'a des unités sur le plateau
            canConquierAdjacent = False
            for cases in case.adjacent:
                if cases.playerOnCase == self:
                    canConquierAdjacent = True
                    #print("On est adjacent")

        if canConquierMer is True:
            canConquier = case.sea

        if canConquierAdjacent and canConquier:
            howManyToConquier = 0
            while case.NumberuniteOnCase > howManyToConquier < self.army.number:
                howManyToConquier += 1

            if 0 < howManyToConquier < case.NumberuniteOnCase:
                print("0 < howManyToConquier < case.NumberuniteOnCase:")
                self.lastAttack = True
                varDice = diceRandom.randomDice()
                if self.army.number + varDice < case.NumberuniteOnCase:
                    print("Fail, pas assez d'unité")
                    return case, "Fail, pas assez d'unité"
            if howManyToConquier > 0:
                self.army.number -= howManyToConquier
                if case.playerOnCase is not None:
                    case.playerOnCase.army.number = case.NumberuniteOnCase - 1
                case.caseAddBeenConquiert(self, howManyToConquier)
            if self.army.number == 0:
                self.lastAttack = True
                print("self.army.number == 0")
            return case, False
        if not canConquier:
            return case, "Ce n'est pas une case mer !"
        elif not canConquierAdjacent:
            return case, "Ce n'est pas une case adjacente !"

    def stack(self, listeCase):
        for cases in listeCase:
            if cases.typeOfUniteOnCase == self.army.race:
                self.army.number += cases.NumberuniteOnCase - 1
                cases.NumberuniteOnCase = 1
        return listeCase

    def replaceArmy(self, case):
        if case.typeOfUniteOnCase == self.army.race:
            case.NumberuniteOnCase += 1
            self.army.number -= 1
            return case
