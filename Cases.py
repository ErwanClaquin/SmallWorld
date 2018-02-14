class Case:
    def __init__(self, adjacent, freePeople, type, moutain, playerOnCase):
        self.adjacent = adjacent
        self.freePepole = freePeople
        self.type = type
        self.playerOnCase = playerOnCase
        self.moutain = moutain
        self.uniteOnCase = 2 + int(self.freePepole)

    def setPlayerOnCase(self, player):
        self.playerOnCase = player

    def setUniteOnCase(self, nombreUnite):
        self.uniteOnCase = nombreUnite

    def caseAddBeenConquiert(self, player):
        self.playerOnCase = player
        self.uniteOnCase = player.nombreUnite

caseMagic = "Magic"
caseNormal = "Normal"
caseShovel = "Shovel"
caseCave = "Cave"

case1 = Case([2, 6], False, caseNormal, True, None)
case2 = Case([1, 6, 7, 8], False, caseMagic, False, None)
case3 = Case([2, 4, 6, 7, 8], False, caseCave, True, None)
case4 = Case([3, 5, 8, 9], False, caseMagic, False, None)
case5 = Case([4, 9, 10], True, caseCave, False, None)
case6 = Case([1, 2, 7, 11], False, caseNormal, False, None)
case7 = Case([2, 3, 6, 8, 11, 12], True, caseShovel, False, None)
case8 = Case([3, 4, 7, 9, 12, 13], False, caseNormal, False, None)
case9 = Case([4, 5, 8, 10, 13, 14], False, caseShovel, True, None)
case10 = Case([5, 9, 14, 15], False, caseNormal, False, None)
case11 = Case([6, 7, 12, 17, 18], True, caseNormal, False, None)
case12 = Case([7, 8, 11, 13, 18, 19], True, caseCave, False, None)
case13 = Case([8, 9, 12, 14, 44], False, caseNormal, True, None)
case14 = Case([9, 10, 13, 15, 44, 45], True, caseCave, False, None)
case15 = Case([10, 14, 45], False, caseShovel, False, None)
case16 = Case([17], True, caseNormal, False, None)
case17 = Case([11, 16, 18, 20], False, caseMagic, False, None)
case18 = Case([11, 12, 17, 19, 20, 21], True, caseNormal, False, None)
case19 = Case([12, 18, 21], False, caseMagic, False, None)
case20 = Case([17, 18, 21, 23, 24], True, caseNormal, False, None)
case21 = Case([18, 19, 20, 24], True, caseShovel, True, None)
case22 = Case([23, 25], False, caseShovel, False, None)
case23 = Case([20, 22, 24, 25, 26], False, caseNormal, False, None)
case24 = Case([20, 21, 23, 26, 27, 31], True, caseNormal, False, None)
case25 = Case([22, 23, 26, 28], True, caseCave, False, None)
case26 = Case([23, 24, 25, 27, 28, 29], True, caseNormal, False, None)
case27 = Case([24, 26, 29, 30, 31], False, caseNormal, False, None)
case28 = Case([25, 26, 29], True, caseShovel, False, None)
case29 = Case([26, 27, 28, 30], True, caseMagic, False, None)
case30 = Case([27, 29, 31, 32], False, caseShovel, False, None)
case31 = Case([24, 27, 30, 32, 33, 34], True, caseCave, False, None)
case32 = Case([30, 31, 33, 35], False, caseMagic, True, None)
case33 = Case([31, 32, 34, 35], False, caseNormal, False, None)
case34 = Case([31, 33, 35, 36, 39], False, caseMagic, False, None)
case35 = Case([32, 33, 34, 36, 37], True, caseNormal, False, None)
case36 = Case([34, 35, 37, 38, 39, 40], True, caseShovel, True, None)
case37 = Case([35, 36, 38], False, caseCave, False, None)
case38 = Case([36, 37, 40, 41], True, caseMagic, False, None)
case39 = Case([34, 36, 40, 43], True, caseNormal, False, None)
case40 = Case([36, 38, 39, 41, 42, 43], False, caseNormal, False, None)
case41 = Case([38, 40, 42], True, caseCave, False, None)
case42 = Case([40, 41, 43, 45], False, caseNormal, False, None)
case43 = Case([39, 40, 42, 44, 45], True, caseShovel, False, None)
case44 = Case([13, 14, 43, 45], False, caseNormal, False, None)
case45 = Case([14, 15, 42, 43, 44], False, caseMagic, True, None)

