from Cases import *
from random import *

class Unite:
    def __init__(self):
        self.number = 0
        self.race = "Aucune"

    def setFall(self, army, listeCaseArmeeVivante):
        for element in army:
            for case in listeCaseArmeeVivante:
                if element in case:
                    case.setUniteOnCase(1)
        self.isFall = True
