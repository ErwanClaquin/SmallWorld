import pygame
from pygame import *


class Games:
    def __init__(self, Initgame, Map):
        self.listeJoueur = Initgame.getListeJoueur()
        self.map = Map
        self.MouseButtonUp = 1
        self.listeCases = Initgame.getListeCases()
        self.map.setListeCase(Initgame.getListeCases())

        self.tour = 0
        self.partieEnCours = True
        self.UniteToBuy = Initgame.uniteToBuy
        self.map.setUnitToBuy(self.UniteToBuy)

    """On considère que lorsqu'un joueur perd il est eliminé, ainsi il restera dans la liste et quand son tour viendra son tour passera automatiquement"""

    def changePlayer(self):
        self.listeJoueur[0].Attack = True
        self.listeJoueur.append(self.listeJoueur[0])
        self.listeJoueur.remove(self.listeJoueur[0])

    def run(self):
        while self.partieEnCours:
            if self.listeJoueur[0].army is None:
                self.chooseUnite()
            else:
                self.map.displayMap()
                self.map.displayUnite()
                for event in pygame.event.get():
                    """On fait la liste de tous les évenements qui peuvent se produirent"""
                    if event.type == QUIT:
                        """Si l'utilisateur clic sur la croix en haut à droite, le programme se ferme"""
                        self.partieEnCours = False
                    if event.type == MOUSEBUTTONUP and event.button == self.MouseButtonUp:
                        if self.listeJoueur[0].Attack:  # Tant qu'il peut attaquer
                            self.clicGaucheAttaque()
                        elif self.listeJoueur[0].Replace:
                            self.cliqueGaucheReplace()
                    if event.type == MOUSEBUTTONUP and event.button == 3:
                        for case in self.listeCases:
                            if case.onCase(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                                print(" joueur :", case.playerOnCase.name, " type", case.typeOfUniteOnCase, " Nombres :",
                                      case.NumberuniteOnCase)

                if not self.listeJoueur[0].Attack and not self.listeJoueur[0].Replace:
                    self.listeJoueur[0].Attack = True
                    self.changePlayer()
                    print("\n","Tour du joueur", self.listeJoueur[0].name)
                pygame.display.flip()
        pygame.quit()

    def clicGaucheAttaque(self):
        for case in self.listeCases:
            if case.onCase(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) and case.playerOnCase != \
                    self.listeJoueur[0]:
                print("sur la case")
                self.listeCases.remove(case)
                case = self.listeJoueur[0].conquier(case)
                self.listeCases.append(case)
                if self.listeJoueur[0].lastAttack:
                    self.listeCases = self.listeJoueur[0].stack(self.listeCases)
                    self.listeJoueur[0].Attack = False
                    self.listeJoueur[0].Replace = True

    def cliqueGaucheReplace(self):
        if self.listeJoueur[0].toReplace > 0:
            for case in self.listeCases:
                if case.onCase(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) and case.playerOnCase == \
                        self.listeJoueur[0]:
                    self.listeCases.remove(case)
                    case = self.listeJoueur[0].replaceArmy(case)
                    print("Après remplacement :", self.listeJoueur[0].toReplace)
                    self.listeCases.append(case)
                    if self.listeJoueur[0].toReplace <= 0:
                        self.listeJoueur[0].Replace = False
                    return

    def cliqueGaucheBuyArmy(self):
        if 0 < pygame.mouse.get_pos()[1] < 75:
            print(self.listeJoueur[0].name, "vous avez acheter des", self.UniteToBuy[0].race, "!")
            self.listeJoueur[0].army = self.UniteToBuy[0]

        if 100 < pygame.mouse.get_pos()[1] < 175 and self.listeJoueur[0].victoryPoint >= 1:
            print(self.listeJoueur[0].name, "vous avez acheter des", self.UniteToBuy[1].race, "!")
            self.listeJoueur[0].army = self.UniteToBuy[1]
            self.listeJoueur[0].victoryPoint -= 1
            self.UniteToBuy.remove(self.UniteToBuy[1])

        if 200 < pygame.mouse.get_pos()[1] < 275 and self.listeJoueur[0].victoryPoint >= 2:
            print(self.listeJoueur[0].name, "vous avez acheter des", self.UniteToBuy[2].race, "!")
            self.listeJoueur[0].army = self.UniteToBuy[2]
            self.listeJoueur[0].victoryPoint -= 2
            self.UniteToBuy.remove(self.UniteToBuy[2])

        if 300 < pygame.mouse.get_pos()[1] < 375 and self.listeJoueur[0].victoryPoint >= 3:
            print(self.listeJoueur[0].name, "vous avez acheter des", self.UniteToBuy[3].race, "!")
            self.listeJoueur[0].army = self.UniteToBuy[3]
            self.listeJoueur[0].victoryPoint -= 3
            self.UniteToBuy.remove(self.UniteToBuy[3])

    def chooseUnite(self):
        self.map.backGround = self.map.shop
        while self.listeJoueur[0].army is None and self.partieEnCours:
            self.map.displayMap()
            self.map.displayShop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.partieEnCours = False
                if event.type == MOUSEBUTTONUP and event.button == self.MouseButtonUp:
                    self.cliqueGaucheBuyArmy()
            pygame.display.flip()
        self.map.backGround = self.map.battelfield

    def addTour(self):
        self.tour += 1
