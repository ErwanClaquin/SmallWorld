from Players import *


class Init:
    def __init__(self):
        self.listeJoueur = []

    def InitJoueur(self):
        NumberPlayer = int(input("Combien de joueur êtes vous ? : "))
        compteJoueur = 0
        while compteJoueur < NumberPlayer:
            joueur = Joueur()
            print("Enterz un nom")
            joueur.setName(input())
            self.listeJoueur.append(joueur)
            compteJoueur += 1
        for j in range(len(self.listeJoueur)):
            print(self.listeJoueur[j].name)

    def CheckNbrJoueur(self, number):
        if number is not int:
            print("Vous n'avez pas rentrer de nombre !")
            return Init.InitJoueur()
        else:
            return
