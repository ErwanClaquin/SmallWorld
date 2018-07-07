from InitGame import *
from Game import *
from Map import *
from decompte import *


InitTheGame = Init()
InitTheGame.InitJoueur()

MapOfTheGame = Map()
MapOfTheGame.start()

myDecompte = decompte(MapOfTheGame)
myDecompte.start()

TheGame = Games(InitTheGame, MapOfTheGame,myDecompte)
TheGame.runGame()
