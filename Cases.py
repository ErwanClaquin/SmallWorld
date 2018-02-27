from DataName import *


class Case:
    def __init__(self, adjacent, freePeople, type, moutain, playerOnCase, typeOfUniteOnCase, x, y):
        self.adjacent = adjacent
        self.freePepole = freePeople
        self.type = type
        self.playerOnCase = playerOnCase
        self.moutain = moutain
        self.uniteOnCase = 2 + int(self.freePepole)
        self.coord = [(x, y), (x + 75, y + 75)]
        self.typeOfUniteOnCase = typeOfUniteOnCase

    def onCase(self, x, y):
        return (self.coord[0][0] < x < self.coord[1][0]) and (self.coord[0][1] < y < self.coord[1][1])


case1 = Case([2, 6], False, caseNormal, True, None, None, 172, 13)
case2 = Case([1, 6, 7, 8], False, caseMagic, False, None, None, 320, 21)
case3 = Case([2, 4, 6, 7, 8], False, caseCave, True, None, None, 453, 27)
case4 = Case([3, 5, 8, 9], False, caseMagic, False, None, None, 573, 24)
case5 = Case([4, 9, 10], True, caseCave, False, None, None, 719, 30)
case6 = Case([1, 2, 7, 11], False, caseNormal, False, None, None, 237, 129)
case7 = Case([2, 3, 6, 8, 11, 12], True, caseShovel, False, None, None, 403, 172)
case8 = Case([3, 4, 7, 9, 12, 13], False, caseNormal, False, None, None, 499, 148)
case9 = Case([4, 5, 8, 10, 13, 14], False, caseShovel, True, None, None, 656, 140)
case10 = Case([5, 9, 14, 15], False, caseNormal, False, None, None, 801, 111)
case11 = Case([6, 7, 12, 17, 18], True, caseNormal, False, None, None, 298, 277)
case12 = Case([7, 8, 11, 13, 18, 19], True, caseCave, False, None, None, 446, 293)
case13 = Case([8, 9, 12, 14, 44], False, caseNormal, True, None, None, 578, 253)
case14 = Case([9, 10, 13, 15, 44, 45], True, caseCave, False, None, None, 733, 262)
case15 = Case([10, 14, 45], False, caseShovel, False, None, None, 867, 243)
case16 = Case([17], True, caseNormal, False, None, None, 85, 335)
case17 = Case([11, 16, 18, 20], False, caseMagic, False, None, None, 203, 374)
case18 = Case([11, 12, 17, 19, 20, 21], True, caseNormal, False, None, None, 341, 399)
case19 = Case([12, 18, 21], False, caseMagic, False, None, None, 455, 411)
case20 = Case([17, 18, 21, 23, 24], True, caseNormal, False, None, None, 240, 495)
case21 = Case([18, 19, 20, 24], True, caseShovel, True, None, None, 362, 525)
case22 = Case([23, 25], False, caseShovel, False, None,None, 12, 551)
case23 = Case([20, 22, 24, 25, 26], False, caseNormal, False, None, None, 142, 604)
case24 = Case([20, 21, 23, 26, 27, 31], True, caseNormal, False, None, None, 277, 658)
case25 = Case([22, 23, 26, 28], True, caseCave, False, None, None, 16, 730)
case26 = Case([23, 24, 25, 27, 28, 29], True, caseNormal, False, None, None, 141, 759)
case27 = Case([24, 26, 29, 30, 31], False, caseNormal, False, None, None, 288, 788)
case28 = Case([25, 26, 29], True, caseShovel, False, None, None, 39, 906)
case29 = Case([26, 27, 28, 30], True, caseMagic, False, None, None, 188, 882)
case30 = Case([27, 29, 31, 32], False, caseShovel, False, None, None, 344, 905)
case31 = Case([24, 27, 30, 32, 33, 34], True, caseCave, False, None, None, 436, 798)
case32 = Case([30, 31, 33, 35], False, caseMagic, True, None, None, 474, 916)
case33 = Case([31, 32, 34, 35], False, caseNormal, False, None, None, 545, 841)
case34 = Case([31, 33, 35, 36, 39], False, caseMagic, False, None, None, 583, 711)
case35 = Case([32, 33, 34, 36, 37], True, caseNormal, False, None, None, 672, 857)
case36 = Case([34, 35, 37, 38, 39, 40], True, caseShovel, True, None, None, 742, 742)
case37 = Case([35, 36, 38], False, caseCave, False, None, None, 821, 860)
case38 = Case([36, 37, 40, 41], True, caseMagic, False, None, None, 877, 720)
case39 = Case([34, 36, 40, 43], True, caseNormal, False, None, None, 690, 619)
case40 = Case([36, 38, 39, 41, 42, 43], False, caseNormal, False, None, None, 802, 594)
case41 = Case([38, 40, 42], True, caseCave, False, None, None, 918, 600)
case42 = Case([40, 41, 43, 45], False, caseNormal, False, None, None, 862, 486)
case43 = Case([39, 40, 42, 44, 45], True, caseShovel, False, None, None, 705, 475)
case44 = Case([13, 14, 43, 45], False, caseNormal, False, None, None, 682, 356)
case45 = Case([14, 15, 42, 43, 44], False, caseMagic, True, None, None, 816, 367)

listeCase = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14,
             case15, case16, case17, case18, case19, case20, case21, case22, case23, case24, case25, case26, case27,
             case28, case29, case30, case31, case32, case33, case34, case35, case36, case37, case38, case39, case40,
             case41, case42, case43, case44, case45]
