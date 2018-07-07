from InitGame import *
from Game import *
from Map import *
from decompte import *


InitTheGame = Init()
InitTheGame.InitJoueur()
MapOfTheGame = Map()
myDecompte = decompte()
myDecompte.start()

TheGame = Games(InitTheGame, MapOfTheGame,myDecompte)
TheGame.runGame()
