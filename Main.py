from InitGame import *
from Game import *
from Map import *
from decompte import *


InitTheGame = Init()

MapOfTheGame = Map()

myDecompte = decompte(MapOfTheGame)


TheGame = Games(InitTheGame, MapOfTheGame,myDecompte)
TheGame.runGame()
