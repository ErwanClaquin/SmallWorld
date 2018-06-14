from Cases import *
from random import *

class Unite:
    def __init__(self):
        self.number = 0
        self.race = "Aucune"
        self.isFall = False

    def Conquier(self, listeCaseArmeeVivante, listeCaseArmeeDeclin, caseArrivee, numberUnite, playerAttack, typeUnite):
        """
        self.move
        while mon nombre courant != 0
            nombre courant = nombre Dispo
            Je joue : J'enlève du nombre courant
        self.stack() càd j'enlève tout sauf 1 sur toutes les cartes occupées


        :return:

        """

        if self.Moves(listeCaseArmeeVivante, listeCaseArmeeDeclin, caseArrivee):
            if self.Attak(caseArrivee, numberUnite):
                numberUnite -= caseArrivee.uniteOnCase
                caseArrivee.uniteOnCase = numberUnite
                caseArrivee.playerOnCase = playerAttack
                caseArrivee.typeOfUniteOnCase = typeUnite
                return True



        return

    def Attak(self, case, numberUnite):
        """
        On a une case avec un attribut qu'on appelle case.NumberUniteToConquier
         on vérifie
         si numberUnite > case.NumberUniteToConquier
            on enlève de nombre courant le nombre d'unité
         sinon
            on réappelle la fonction, avec un dé de (0,0,1,1,2,3) pour tenter de reconquérir la case.
        :return:
        """
        des = [0,0,1,1,2,3]

        if numberUnite > case.uniteOnCase :
            return True
        else :
            if numberUnite > 0 :
                uniteSuppplementaire = random.randint(des)
                numberUnite += uniteSuppplementaire
                if numberUnite > case.uniteOnCase :
                    if uniteSuppplementaire > 0:
                        for i in range (0, uniteSuppplementaire):
                            if case.uniteOnCase - 1 >= 1 :
                                case.uniteOnCase -= 1
                    numberUnite -= uniteSuppplementaire
                    return True


        return False

    def Stack(self,listeCaseArmeeVivante):
        """
        on reprends toutes les unitées sauf 1 par case et on les remets


        :return:
        """

        for case in listeCaseArmeeVivante :
            if Unite.number > 1 :
                Unite.number += case.uniteOnCase - 1

        return Unite.number

    def Moves(self, listeCaseArmeeVivante, listeCaseArmeeDeclin, caseArrivee):
        "On prend les coordonnées de la case sur laquelle on clique pour savoir si on peut se déplacer sur cette case."
        "Inutile de savoir toutes les cases possible seule la case sur laquelle le joueur veut se déplacer est importante"
        "Il faut vérifier si la case d'arrivée est adjactentes à au moins case ocupée par le joueur"
        """Je conquéris
                si rien sur plateau:
                    à côté de mer
                sinon
                    à côté d'une case occupée
                :return:"""

        if listeCaseArmeeVivante == [] and caseArrivee.border and caseArrivee not in listeCaseArmeeDeclin:
            return True

        for case in listeCaseArmeeVivante:
            if caseArrivee in case.adjacent and caseArrivee not in listeCaseArmeeDeclin:
                return True

        return False




    def setFall(self, army, listeCaseArmeeVivante):
        for element in army:
            for case in listeCaseArmeeVivante:
                if element in case:
                    case.setUniteOnCase(1)
        self.isFall = True
