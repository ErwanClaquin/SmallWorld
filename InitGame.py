from Players import *
from Map import *
from Cases import *

from Amazon import *
from Dwarf import *
from Elf import *
from Giant import *
from Hobbit import *
from Humans import *
from Mago import *
from Orc import *
from Rats import *
from Skeletton import *
from Triton import *
from Troll import *
from Wizzard import *
from Zombie import *

from random import *


class Init:
    def __init__(self):
        self.listeJoueur = []
        self.listeCases = []
        self.createsCases()
        self.uniteToBuy = []
        self.createUnitToBuy()

    def InitJoueur(self):
        # NumberPlayer = input("Combien de joueur êtes vous ? : ")
        NumberPlayer = 2
        verif = self.CheckNbrJoueur(NumberPlayer)
        if verif:
            NumberPlayer = int(NumberPlayer)
            compteJoueur = 0
            while compteJoueur < NumberPlayer:
                self.CreatePlayer()
                compteJoueur += 1
        elif not verif:
            self.InitJoueur()

    def CreatePlayer(self):
        joueur = Joueur()
        print("Entrez un nom : ")
        joueur.name = 'e'
        self.listeJoueur.append(joueur)

    def CheckNbrJoueur(self, number):
        try:
            int(number)
        except ValueError:
            print("Vous n'avez pas rentrer de nombre !")
            return False
        else:
            return True

    def getListeJoueur(self):
        return self.listeJoueur

    def createUnitToBuy(self):
        self.uniteToBuy = [Amazon(), Dwarf(), Elf(), Giant(), Hobbit(), Humans(), Mago(), Orc(), Rats(), Skeletton(),
                           Triton(), Troll(), Wizzard(), Zombie()]
        shuffle(self.uniteToBuy)

    def associatePower(self):
        # Todo : faire les pouvoirs spéciaux
        return

    def createsCases(self):
        case1 = Case([2, 6], 0, caseNormal, True, None, None, 172, 13, True)
        case2 = Case([1, 6, 7, 8], 0, caseMagic, False, None, None, 320, 21, False)
        case3 = Case([2, 4, 6, 7, 8], 0, caseCave, True, None, None, 453, 27, False)
        case4 = Case([3, 5, 8, 9], 0, caseMagic, False, None, None, 573, 24, False)
        case5 = Case([4, 9, 10], 1, caseCave, False, None, None, 719, 30, False)
        case6 = Case([1, 2, 7, 11], 0, caseNormal, False, None, None, 237, 129, True)
        case7 = Case([2, 3, 6, 8, 11, 12], 1, caseShovel, False, None, None, 403, 172, False)
        case8 = Case([3, 4, 7, 9, 12, 13], 0, caseNormal, False, None, None, 499, 148, False)
        case9 = Case([4, 5, 8, 10, 13, 14], 0, caseShovel, True, None, None, 656, 140, False)
        case10 = Case([5, 9, 14, 15], 0, caseNormal, False, None, None, 801, 111, False)
        case11 = Case([6, 7, 12, 17, 18], 1, caseNormal, False, None, None, 298, 277, True)
        case12 = Case([7, 8, 11, 13, 18, 19], 1, caseCave, False, None, None, 446, 293, True)
        case13 = Case([8, 9, 12, 14, 44], 0, caseNormal, True, None, None, 578, 253, True)
        case14 = Case([9, 10, 13, 15, 44, 45], 1, caseCave, False, None, None, 733, 262, False)
        case15 = Case([10, 14, 45], 0, caseShovel, False, None, None, 867, 243, False)
        case16 = Case([17], 1, caseNormal, False, None, None, 85, 335, True)
        case17 = Case([11, 16, 18, 20], 0, caseMagic, False, None, None, 203, 374, True)
        case18 = Case([11, 12, 17, 19, 20, 21], True, caseNormal, False, None, None, 341, 399, False)
        case19 = Case([12, 18, 21], 0, caseMagic, False, None, None, 455, 411, True)
        case20 = Case([17, 18, 21, 23, 24], True, caseNormal, False, None, None, 240, 495, True)
        case21 = Case([18, 19, 20, 24], True, caseShovel, True, None, None, 362, 525, True)
        case22 = Case([23, 25], 0, caseShovel, False, None, None, 12, 551, True)
        case23 = Case([20, 22, 24, 25, 26], 0, caseNormal, False, None, None, 142, 604, True)
        case24 = Case([20, 21, 23, 26, 27, 31], True, caseNormal, False, None, None, 277, 658, True)
        case25 = Case([22, 23, 26, 28], 1, caseCave, False, None, None, 16, 730, False)
        case26 = Case([23, 24, 25, 27, 28, 29], True, caseNormal, False, None, None, 141, 759, False)
        case27 = Case([24, 26, 29, 30, 31], 0, caseNormal, False, None, None, 288, 788, False)
        case28 = Case([25, 26, 29], 1, caseShovel, False, None, None, 39, 906, False)
        case29 = Case([26, 27, 28, 30], 1, caseMagic, False, None, None, 188, 882, False)
        case30 = Case([27, 29, 31, 32], 0, caseShovel, False, None, None, 344, 905, False)
        case31 = Case([24, 27, 30, 32, 33, 34], True, caseCave, False, None, None, 436, 798, True)
        case32 = Case([30, 31, 33, 35], 0, caseMagic, True, None, None, 474, 916, False)
        case33 = Case([31, 32, 34, 35], 0, caseNormal, False, None, None, 545, 841, False)
        case34 = Case([31, 33, 35, 36, 39], 0, caseMagic, False, None, None, 583, 711, True)
        case35 = Case([32, 33, 34, 36, 37], 1, caseNormal, False, None, None, 672, 857, False)
        case36 = Case([34, 35, 37, 38, 39, 40], 1, caseShovel, True, None, None, 742, 742, False)
        case37 = Case([35, 36, 38], 0, caseCave, False, None, None, 821, 860, True)
        case38 = Case([36, 37, 40, 41], 1, caseMagic, False, None, None, 877, 720, True)
        case39 = Case([34, 36, 40, 43], 1, caseNormal, False, None, None, 690, 619, True)
        case40 = Case([36, 38, 39, 41, 42, 43], 0, caseNormal, False, None, None, 802, 594, False)
        case41 = Case([38, 40, 42], 1, caseCave, False, None, None, 918, 600, False)
        case42 = Case([40, 41, 43, 45], 0, caseNormal, False, None, None, 862, 486, False)
        case43 = Case([39, 40, 42, 44, 45], 1, caseShovel, False, None, None, 705, 475, True)
        case44 = Case([13, 14, 43, 45], 0, caseNormal, False, None, None, 682, 356, True)
        case45 = Case([14, 15, 42, 43, 44], 0, caseMagic, True, None, None, 816, 367, False)

        case1.adjacent = [case2, case6]
        case2.adjacent = [case1, case6, case7, case8]
        case3.adjacent = [case2, case4, case6, case7, case8]
        case4.adjacent = [case3, case5, case8, case9]
        case5.adjacent = [case4, case9, case10]
        case6.adjacent = [case1, case2, case7, case11]
        case7.adjacent = [case2, case3, case6, case8, case11, case12]
        case8.adjacent = [case3, case4, case7, case9, case12, case13]
        case9.adjacent = [case4, case5, case8, case10, case13, case14]
        case10.adjacent = [case5, case9, case14, case15]
        case11.adjacent = [case6, case7, case12, case17, case18]
        case12.adjacent = [case7, case8, case11, case13, case18, case19]
        case13.adjacent = [case8, case9, case12, case14, case44]
        case14.adjacent = [case9, case10, case13, case15, case44]
        case15.adjacent = [case10, case14, case45]
        case16.adjacent = [case17]
        case17.adjacent = [case11, case16, case18, case20]
        case18.adjacent = [case11, case12, case17, case19, case20, case21]
        case19.adjacent = [case12, case18, case21]
        case20.adjacent = [case17, case18, case21, case23, case24]
        case21.adjacent = [case18, case19, case20, case24]
        case22.adjacent = [case23, case25]
        case23.adjacent = [case20, case22, case24, case25, case26]
        case24.adjacent = [case20, case21, case23, case26, case27, case31]
        case25.adjacent = [case22, case23, case26, case28]
        case26.adjacent = [case23, case24, case25, case27, case28, case29]
        case27.adjacent = [case24, case26, case29, case30, case31]
        case28.adjacent = [case25, case26, case29]
        case29.adjacent = [case26, case27, case28, case30]
        case30.adjacent = [case27, case29, case31, case32]
        case31.adjacent = [case24, case27, case30, case32, case33, case34]
        case32.adjacent = [case30, case31, case33, case35]
        case33.adjacent = [case31, case32, case34, case35]
        case34.adjacent = [case31, case33, case35, case36, case39]
        case35.adjacent = [case32, case33, case34, case36, case37]
        case36.adjacent = [case34, case35, case37, case38, case39, case40]
        case37.adjacent = [case35, case36, case38]
        case38.adjacent = [case36, case37, case40, case41]
        case39.adjacent = [case34, case36, case40, case43]
        case40.adjacent = [case36, case38, case39, case41, case42, case43]
        case41.adjacent = [case38, case40, case42]
        case42.adjacent = [case40, case41, case43, case45]
        case43.adjacent = [case39, case40, case42, case44, case45]
        case44.adjacent = [case13, case14, case43, case45]
        case45.adjacent = [case14, case15, case42, case43, case44]

        self.listeCases = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12,
                           case13, case14, case15, case16, case17, case18, case19, case20, case21, case22, case23,
                           case24, case25, case26, case27, case28, case29, case30, case31, case32, case33, case34,
                           case35, case36, case37, case38, case39, case40, case41, case42, case43, case44, case45]

    def getListeCases(self):
        return self.listeCases
