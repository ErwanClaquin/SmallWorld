from threading import Thread, RLock
import time


class decompte (Thread):

    def __init__(self,MapOfTheGame):
        Thread.__init__(self)
        self.decomptejoueur=0
        self.keepAlive = True
        self.myMapOfTheGame=MapOfTheGame
        self.start()

    def run(self):
        while(self.keepAlive):
            self.decomptejoueur = self.decomptejoueur +1
            self.myMapOfTheGame.myAffichageDecompe = self.decomptejoueur
            time.sleep(1)

    def changementDeJoueur(self):
        self.decomptejoueur = 0
        self.myMapOfTheGame.myAffichageDecompe = self.decomptejoueur

    def stopDecompte(self):
        self.keepAlive=False