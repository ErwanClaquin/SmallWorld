from Cases import *

class Unite:
    def __init__(self):
        self.number = 0
        self.race = "Aucune"

    def Conquier(self):
        """
        self.move
        while mon nombre courant != 0
            nombre courant = nombre Dispo
            Je joue : J'enlève du nombre courant
        self.stack() càd j'enlève tout sauf 1 sur toutes les cartes occupées


        :return:

        """

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
        return

    def Stack(self):
        """
        on reprends toutes les unitées sauf 1 par case et on les remets


        :return:
        """
        return


    def Moves(self, listeCaseOccupee, typeCase, caseArrivee) :
        "On prend les coordonnées de la case sur laquelle on clique pour savoir si on peut se déplacer sur cette case."
        "Inutile de savoir toutes les cases possible seule la case sur laquelle le joueur veut se déplacer est importante"
        "Il faut vérifier si la case d'arrivée est adjactentes à au moins case ocupée par le joueur"
        """Je conquéris
                si rien sur plateau:
                    à côté de mer
                sinon
                    à côté d'une case occupée
                :return:"""

        #if cliqueGauche == True
        try :
            if typeCase == "mer" :
                raise TypeError("C'est une case mer")
            else :
                for element in listeCaseOccupee:
                    if caseArrivee in listeCaseOccupee :
                        return False
                    if caseArrivee in Case.getAdjacent(element) :
                        return True
        except TypeError :
            print("Ce n'est pas une case mer")

