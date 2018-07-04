from InitGame import *
from Game import *
from Map import *

InitTheGame = Init()
InitTheGame.InitJoueur()
MapOfTheGame = Map()

TheGame = Games(InitTheGame, MapOfTheGame)
TheGame.runGame()
