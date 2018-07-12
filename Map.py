import pygame
from DataName import *
from threading import Thread, RLock

import time
from pygame.locals import *

verrou = RLock()


class Map(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.ecran = pygame.display.set_mode((1396, 1096))
        self.shop = pygame.image.load("Shop.jpg").convert()
        self.battelfield = pygame.image.load("small_world1.jpg").convert()
        self.border = pygame.image.load("Border.png").convert()
        self.under = pygame.image.load("under.jpg").convert()
        self.backGround = self.battelfield

        self.currentPlayer = None
        self.log = ""

        # Image of Unites
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
        self.listeCase = []
        self.shop = pygame.image.load("Shop.jpg").convert()
        self.UnitToBuy = []

        self.keepAlive = True
        self.myAffichageDecompe = ""
        pygame.init()
        # font.init()

    def run(self):
        while (self.keepAlive):
            if self.currentPlayer != None:
                if self.currentPlayer.army is None:
                    self.backGround = self.shop
                else:
                    self.backGround = self.battelfield
                with verrou:
                    self.displayMap()
                    self.affichageData()
                    if self.backGround != self.shop:
                        self.displayUnite()
                        self.affichageNumberOncase()
                    else:
                        self.displayShop()
                    pygame.display.flip()
            time.sleep(0.25)  # Todo : Voir comment gérer les clignotemenst : plus c'est petit plus ça clignote

    def changeLog(self, log):
        self.log = log

    def refreshData(self, player):
        self.currentPlayer = player

    def affichageNumberOncase(self):
        for case in self.listeCase:
            if case.typeOfUniteOnCase is not None:
                text = str(case.NumberuniteOnCase)
                font = pygame.font.Font(None, 30)
                textImage = font.render(text, False, (255, 0, 0))
                self.ecran.blit(textImage, case.coord[0])

    def affichageData(self):

        ####Decompte####
        text = "temps de jeu = " + str(self.myAffichageDecompe)
        font = pygame.font.Font(None, 30)
        textImage = font.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage, (1050, 20))


        ####PlayerName####

        text = "Joueur : " + str(self.currentPlayer.name)
        font1 = pygame.font.Font(None, 30)
        textImage1 = font1.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage1, (1050, 40))


        ####PlayerArmyName####

        if self.currentPlayer.army is None:
            text = "Pas d'armée"
        else:
            text = "Armée : " + str(self.currentPlayer.army.race)
        font2 = pygame.font.Font(None, 30)
        textImage2 = font2.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage2, (1050, 60))


        ####PlayerNumerArmyName####

        if self.currentPlayer.army is None:
            text = "Pas d'armée"
        else:
            text = "Nombre dans l'Armée : " + str(self.currentPlayer.army.number)
        font3 = pygame.font.Font(None, 30)
        textImage3 = font3.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage3, (1050, 80))


        ####PlayerActionToDo####

        text = "Action : " + self.WhichAction()
        font4 = pygame.font.Font(None, 30)
        textImage4 = font4.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage4, (1050, 100))


        ####Log####

        text = self.log
        font5 = pygame.font.Font(None, 50)
        textImage5 = font5.render(text, False, (255, 0, 0))
        self.ecran.blit(textImage5, (10, 1030))

    def WhichAction(self):
        if self.currentPlayer.Attack is True:
            return "Attaque"
        else:
            return "Remplace"

    def setListeCase(self, listeCase):
        self.listeCase = listeCase

    def setUnitToBuy(self, listUniteToBuy):
        self.UnitToBuy = listUniteToBuy

    def displayMap(self):
        self.ecran.blit(self.border, (900, 0))
        self.ecran.blit(self.under, (0, 547))
        self.ecran.blit(self.backGround, (0, 0))

    def displayShop(self):
        if self.UnitToBuy[0].race == nameAmazon:
            self.ecran.blit(self.Amazon, (0, 0))
        elif self.UnitToBuy[0].race == nameDwarf:
            self.ecran.blit(self.Dwarf, (0, 0))
        elif self.UnitToBuy[0].race == nameElf:
            self.ecran.blit(self.Elf, (0, 0))
        elif self.UnitToBuy[0].race == nameGiant:
            self.ecran.blit(self.Giant, (0, 0))
        elif self.UnitToBuy[0].race == nameHobbit:
            self.ecran.blit(self.Hobbit, (0, 0))
        elif self.UnitToBuy[0].race == nameHumans:
            self.ecran.blit(self.Humans, (0, 0))
        elif self.UnitToBuy[0].race == nameMago:
            self.ecran.blit(self.Mago, (0, 0))
        elif self.UnitToBuy[0].race == nameOrc:
            self.ecran.blit(self.Orc, (0, 0))
        elif self.UnitToBuy[0].race == nameRats:
            self.ecran.blit(self.Rats, (0, 0))
        elif self.UnitToBuy[0].race == nameSkeletton:
            self.ecran.blit(self.Skeletton, (0, 0))
        elif self.UnitToBuy[0].race == nameTriton:
            self.ecran.blit(self.Triton, (0, 0))
        elif self.UnitToBuy[0].race == nameTroll:
            self.ecran.blit(self.Troll, (0, 0))
        elif self.UnitToBuy[0].race == nameWizzard:
            self.ecran.blit(self.Wizzard, (0, 0))
        elif self.UnitToBuy[0].race == nameZombie:
            self.ecran.blit(self.Zombie, (0, 0))

        if self.UnitToBuy[1].race == nameAmazon:
            self.ecran.blit(self.Amazon, (0, 100))
        elif self.UnitToBuy[1].race == nameDwarf:
            self.ecran.blit(self.Dwarf, (0, 100))
        elif self.UnitToBuy[1].race == nameElf:
            self.ecran.blit(self.Elf, (0, 100))
        elif self.UnitToBuy[1].race == nameGiant:
            self.ecran.blit(self.Giant, (0, 100))
        elif self.UnitToBuy[1].race == nameHobbit:
            self.ecran.blit(self.Hobbit, (0, 100))
        elif self.UnitToBuy[1].race == nameHumans:
            self.ecran.blit(self.Humans, (0, 100))
        elif self.UnitToBuy[1].race == nameMago:
            self.ecran.blit(self.Mago, (0, 100))
        elif self.UnitToBuy[1].race == nameOrc:
            self.ecran.blit(self.Orc, (0, 100))
        elif self.UnitToBuy[1].race == nameRats:
            self.ecran.blit(self.Rats, (0, 100))
        elif self.UnitToBuy[1].race == nameSkeletton:
            self.ecran.blit(self.Skeletton, (0, 100))
        elif self.UnitToBuy[1].race == nameTriton:
            self.ecran.blit(self.Triton, (0, 100))
        elif self.UnitToBuy[1].race == nameTroll:
            self.ecran.blit(self.Troll, (0, 100))
        elif self.UnitToBuy[1].race == nameWizzard:
            self.ecran.blit(self.Wizzard, (0, 100))
        elif self.UnitToBuy[1].race == nameZombie:
            self.ecran.blit(self.Zombie, (0, 100))

        if self.UnitToBuy[2].race == nameAmazon:
            self.ecran.blit(self.Amazon, (0, 200))
        elif self.UnitToBuy[2].race == nameDwarf:
            self.ecran.blit(self.Dwarf, (0, 200))
        elif self.UnitToBuy[2].race == nameElf:
            self.ecran.blit(self.Elf, (0, 200))
        elif self.UnitToBuy[2].race == nameGiant:
            self.ecran.blit(self.Giant, (0, 200))
        elif self.UnitToBuy[2].race == nameHobbit:
            self.ecran.blit(self.Hobbit, (0, 200))
        elif self.UnitToBuy[2].race == nameHumans:
            self.ecran.blit(self.Humans, (0, 200))
        elif self.UnitToBuy[2].race == nameMago:
            self.ecran.blit(self.Mago, (0, 200))
        elif self.UnitToBuy[2].race == nameOrc:
            self.ecran.blit(self.Orc, (0, 200))
        elif self.UnitToBuy[2].race == nameRats:
            self.ecran.blit(self.Rats, (0, 200))
        elif self.UnitToBuy[2].race == nameSkeletton:
            self.ecran.blit(self.Skeletton, (0, 200))
        elif self.UnitToBuy[2].race == nameTriton:
            self.ecran.blit(self.Triton, (0, 200))
        elif self.UnitToBuy[2].race == nameTroll:
            self.ecran.blit(self.Troll, (0, 200))
        elif self.UnitToBuy[2].race == nameWizzard:
            self.ecran.blit(self.Wizzard, (0, 200))
        elif self.UnitToBuy[2].race == nameZombie:
            self.ecran.blit(self.Zombie, (0, 200))

        if self.UnitToBuy[3].race == nameAmazon:
            self.ecran.blit(self.Amazon, (0, 300))
        elif self.UnitToBuy[3].race == nameDwarf:
            self.ecran.blit(self.Dwarf, (0, 300))
        elif self.UnitToBuy[3].race == nameElf:
            self.ecran.blit(self.Elf, (0, 300))
        elif self.UnitToBuy[3].race == nameGiant:
            self.ecran.blit(self.Giant, (0, 300))
        elif self.UnitToBuy[3].race == nameHobbit:
            self.ecran.blit(self.Hobbit, (0, 300))
        elif self.UnitToBuy[3].race == nameHumans:
            self.ecran.blit(self.Humans, (0, 300))
        elif self.UnitToBuy[3].race == nameMago:
            self.ecran.blit(self.Mago, (0, 300))
        elif self.UnitToBuy[3].race == nameOrc:
            self.ecran.blit(self.Orc, (0, 300))
        elif self.UnitToBuy[3].race == nameRats:
            self.ecran.blit(self.Rats, (0, 300))
        elif self.UnitToBuy[3].race == nameSkeletton:
            self.ecran.blit(self.Skeletton, (0, 300))
        elif self.UnitToBuy[3].race == nameTriton:
            self.ecran.blit(self.Triton, (0, 300))
        elif self.UnitToBuy[3].race == nameTroll:
            self.ecran.blit(self.Troll, (0, 300))
        elif self.UnitToBuy[3].race == nameWizzard:
            self.ecran.blit(self.Wizzard, (0, 300))
        elif self.UnitToBuy[3].race == nameZombie:
            self.ecran.blit(self.Zombie, (0, 300))

    def displayUnite(self):
        for case in self.listeCase:
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
