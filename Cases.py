from DataName import *


class Case:
    def __init__(self, adjacent, freePeople, type, moutain, playerOnCase, typeOfUniteOnCase, x, y):
        self.adjacent = adjacent
        self.freePepole = freePeople
        self.type = type
        self.playerOnCase = playerOnCase
        self.moutain = moutain
        self.NumberuniteOnCase = 2 + int(self.freePepole)
        self.coord = [(x, y), (x + 75, y + 75)]
        self.typeOfUniteOnCase = typeOfUniteOnCase

    def onCase(self, x, y):
        return (self.coord[0][0] < x < self.coord[1][0]) and (self.coord[0][1] < y < self.coord[1][1])

    def caseAddBeenConquiert(self, player, number):
        self.playerOnCase = player
        self.typeOfUniteOnCase = player.army.race
        self.NumberuniteOnCase = number

