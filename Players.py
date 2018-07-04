from Dice import *


class Joueur:
    def __init__(self):
        self.name = "Default"
        self.army = None
        self.victoryPoint = 5
        self.Attack = True
        self.Replace = False
        self.lastAttack = False
        self.listCaseTemp = []

    def conquier(self, case):
        howManyToConquier = 0
        while case.NumberuniteOnCase > howManyToConquier < self.army.number:
            howManyToConquier += 1
        print("nécessaire pour conquérir : ", case.NumberuniteOnCase, "Possède :", howManyToConquier, "Armée :",
              self.army.number, "Nouvelle armée :", self.army.number - howManyToConquier)

        if howManyToConquier < case.NumberuniteOnCase and howManyToConquier > 0:
            self.lastAttack = True
            varDice = diceRandom.randomDice()
            if self.army.number + varDice < case.NumberuniteOnCase:
                print("Fail, pas assez d'unité")
                return case
        if howManyToConquier > 0:
            self.army.number -= howManyToConquier
            case.caseAddBeenConquiert(self, howManyToConquier)
        if self.army.number == 0:
            self.lastAttack = True
        return case

    def stack(self, listeCase):
        for cases in listeCase:
            if cases.typeOfUniteOnCase == self.army.race:
                print('nombre sur la case :', cases.NumberuniteOnCase)
                #listeCase.remove(cases)
                self.army.number += cases.NumberuniteOnCase - 1
                print("à remplaceer :", self.army.number)
                cases.NumberuniteOnCase = 1
                #listeCase.append(cases)
        print("remplacement dispo :", self.army.number)
        return listeCase

    def replaceArmy(self, case):
        if case.typeOfUniteOnCase == self.army.race:
            case.NumberuniteOnCase += 1
            self.army.number -= 1
            print("reste à remplacer", self.army.number, "unité(s)")
            return case
