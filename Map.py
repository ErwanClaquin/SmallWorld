import pygame
from pygame import *


class Map:
    def __init__(self):
        self.ecran = pygame.display.set_mode((0, 0), RESIZABLE)
        self.ecran_rect = self.ecran.get_rect()
        self.backGround = pygame.image.load("small_world1.jpg").convert()
        self.backGround = pygame.transform.smoothscale(self.backGround, (self.ecran_rect.right, self.ecran_rect.right - self.ecran_rect.right // 10))
        self.tour = 0
    def createMap(self):
        """if nbrJoueur < 3:

            else:
            backGround = " "
        """

        self.ecran.blit(self.backGround, (0, 0))

    def addTour(self):
        self.tour += 1

    def runMap(self):
        partieEnCours = True
        while partieEnCours:
            self.createMap()
            pygame.display.flip()
            for event in pygame.event.get():
                """On fait la liste de tous les évenements qui peuvent se produirent"""
                if event.type == QUIT:
                    """Si l'utilisateur clic sur la croix en haut à droite, le programme se ferme"""
                    partieEnCours = False
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    partieEnCours = False
        pygame.quit()


