import pygame
from pygame import *

class Games:
    def __init__(self, Initgame, Map):
        self.listeJoueur = Initgame.getListeJoueur()
        self.map = Map
        self.MouseButtonUp = 1
        self.map.setListeCase(Initgame.getListeCases())

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
                    self.map.clicGauche()
            pygame.display.flip()
        pygame.quit()
