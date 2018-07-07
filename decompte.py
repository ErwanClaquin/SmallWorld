from threading import Thread, RLock
import time

class decompte (Thread):

    def __init__(self,MapOfTheGame):
        Thread.__init__(self)
        self.decomptejoueur=0
        self.keepAlive = True
        self.myMapOfTheGame=MapOfTheGame

    def run(self):
        while(self.keepAlive):
            self.decomptejoueur = self.decomptejoueur +1
            #print (self.decomptejoueur)
            self.myMapOfTheGame.afficheDecompte(self.decomptejoueur)
            time.sleep(1)

    def changementDeJoueur(self):
        self.decomptejoueur = 0
        self.myMapOfTheGame.afficheDecompte(self.decomptejoueur)
        #print(self.decomptejoueur)

    def stopDecompte(self):
        self.keepAlive=False