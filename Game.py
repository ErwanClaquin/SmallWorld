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

    """On considère que lorsqu'un joueur perd il est eliminé, ainsi il restera dans la liste et quand son tour viendra son tour passera automatiquement"""

    def changePlayer(self):
        self.listeJoueur.append(self.listeJoueur[0])
        self.listeJoueur.remove(self.listeJoueur[0])

    def run(self):
        partieEnCours = True
        while partieEnCours:
            self.map.displayMap()
            self.map.displayUnite()
            for event in pygame.event.get():
                """On fait la liste de tous les évenements qui peuvent se produirent"""
                if event.type == QUIT:
                    """Si l'utilisateur clic sur la croix en haut à droite, le programme se ferme"""
                    partieEnCours = False
                if event.type == MOUSEBUTTONUP and event.button == self.MouseButtonUp:
                    if self.listeJoueur[0].Attack:  # Tant qu'il peut attaquer
                        self.clicGaucheAttaque()
                    elif self.listeJoueur[0].Replace:  # Si il peut changer ses unitées
                        self.cliqueGaucheReplace()
                    else:
                        self.changePlayer()
            pygame.display.flip()
        pygame.quit()

    def clicGaucheAttaque(self):
        for case in self.listeCases:
            if case.onCase(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                self.listeCases.remove(case)
                case, self.listeCases = self.listeJoueur[0].conquier(case, self.listeCases)
                self.listeCases.append(case)
                if self.listeJoueur[0].lastAttack:
                    self.listeCases = self.listeJoueur[0].stack(self.listeCases)
                    self.listeJoueur[0].Attack = False
                    self.listeJoueur[0].Replace = True

    def cliqueGaucheReplace(self):
        for case in self.listeCases:
            if case.onCase(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                self.listeCases.remove(case)
                case = self.listeJoueur[0].replaceArmy()
                self.listeCases.append(case)
                if self.listeJoueur[0].toReplace == 0:
                    self.listeJoueur[0].Attack = True
                    self.listeJoueur[0].Replace = False

    def addTour(self):
        self.tour += 1
