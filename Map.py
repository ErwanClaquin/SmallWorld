import pygame
from DataName import *



class Map:
    def __init__(self):
        self.ecran = pygame.display.set_mode((1396, 996))
        self.shop = pygame.image.load("Shop.jpg").convert()
        self.battelfield = pygame.image.load("small_world1.jpg").convert()
        self.backGround = self.battelfield


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

    def setListeCase(self, listeCase):
        self.listeCase = listeCase

    def setUnitToBuy(self, listUniteToBuy):
        self.UnitToBuy = listUniteToBuy

    def displayMap(self):
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

