import pygame
from pygame import *
from Research import *
from Cases import *
from DataName import *

class Map:
    def __init__(self):
        self.ecran = pygame.display.set_mode((996, 996))
        self.backGround = pygame.image.load("small_world1.jpg").convert()
        self.tour = 0
        #Image of Unites
        self.Amazon = pygame.image.load("Amazon.png").convert()
        self.Dwarf = pygame.image.load("Dwarf.png").convert()
        self.Elf = pygame.image.load("Elf.png").convert()
        self.Giant = pygame.image.load("Giant.png").convert()
        self.Hobbit = pygame.image.load("Hobbit.png").convert()
        self.Humans = pygame.image.load("Humans.png").convert()
        self.Mago = pygame.image.load("Mago.png").convert()
        self.Orc = pygame.image.load("Orc.png").convert()
        self.Rats = pygame.image.load("Rats.png").convert()
        self.Skeletton = pygame.image.load("Skeletton.png").convert()
        self.Triton = pygame.image.load("Triton.png").convert()
        self.Troll = pygame.image.load("Troll.png").convert()
        self.Wizzard = pygame.image.load("Wizzard.png").convert()
        self.Zombie = pygame.image.load("Zombie.png").convert()

    def createMap(self):
        """if nbrJoueur < 3:

            else:
            backGround = " "
        """

        self.ecran.blit(self.backGround, (0, 0))

    def addTour(self):
        self.tour += 1


    def displayUnite(self):
        for case in listeCase:
            if case.typeOfUniteOnCase == nameAmazon:
                self.ecran.blit(self.Amazon, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameDwarf:
                self.ecran.blit(self.Dwarf, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameElf:
                self.ecran.blit(self.Elf, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameGiant:
                self.ecran.blit(self.Giant, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameHobbit:
                self.ecran.blit(self.Hobbit, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameHumans:
                self.ecran.blit(self.Humans, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameMago:
                self.ecran.blit(self.Mago, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameOrc:
                self.ecran.blit(self.Orc, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameRats:
                self.ecran.blit(self.Rats, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameSkeletton:
                self.ecran.blit(self.Skeletton, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameTriton:
                self.ecran.blit(self.Triton, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameTroll:
                self.ecran.blit(self.Troll, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameWizzard:
                self.ecran.blit(self.Wizzard, (case.coord[0], case.coord[1]))
            elif case.typeOfUniteOnCase == nameZombie:
                self.ecran.blit(self.Zombie, (case.coord[0], case.coord[1]))


    def clicGauche(self):
        for cases in listeCase:
            cases.typeOfUniteOnCase = nameAmazon
            print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    def runMap(self):
        partieEnCours = True
        while partieEnCours:
            self.createMap()
            self.displayUnite()
            pygame.display.flip()
            for event in pygame.event.get():
                """On fait la liste de tous les évenements qui peuvent se produirent"""
                if event.type == QUIT:
                    """Si l'utilisateur clic sur la croix en haut à droite, le programme se ferme"""
                    partieEnCours = False
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    self.clicGauche()
                    pygame.display.flip()
        pygame.quit()
