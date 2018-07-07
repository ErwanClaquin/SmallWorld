import pygame
from threading import Thread, RLock

class dataToShow(Thread):
   def __init__(self):
       Thread.__init__(self)
       self.armyName = None
       self.armyNumber = None
       self.ecran = None
       self.playerName = None
       self.armyFallName = None
