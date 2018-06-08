from Players import *
from Map import *


class Init:
    def __init__(self):
        self.listeJoueur = []

    def InitJoueur(self):
        #NumberPlayer = input("Combien de joueur êtes vous ? : ")
        NumberPlayer = 0
        verif = self.CheckNbrJoueur(NumberPlayer)
        if verif:
            NumberPlayer = int(NumberPlayer)
            compteJoueur = 0
            while compteJoueur < NumberPlayer:
                self.CreatePlayer()
                compteJoueur += 1
            self.LauchGame()
        elif not verif:
            self.InitJoueur()

    def CreatePlayer(self):
        joueur = Joueur()
        print("Entrez un nom : ")
        joueur.name = input()
        self.listeJoueur.append(joueur)

    def CheckNbrJoueur(self, number):
        try:
            int(number)
        except ValueError:
            print("Vous n'avez pas rentrer de nombre !")
            return False
        else:
            return True

    def LauchGame(self):
        Fond = Map()
        Fond.createMap()
        Fond.runMap()


Init = Init()
