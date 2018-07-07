from threading import Thread, RLock
import time

class decompte (Thread):

    def __init__(self):
        Thread.__init__(self)
        self.decomptejoueur=0
        self.keepAlive = True
    def run(self):
        while(self.keepAlive):
            self.decomptejoueur = self.decomptejoueur +1
            print (self.decomptejoueur)
            time.sleep(1)

    def changementDeJoueur(self):
        self.decomptejoueur = 0
        print(self.decomptejoueur)

    def stopDecompte(self):
        self.keepAlive=False