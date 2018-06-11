import InitGame


class Game:
    """On considère que lorsqu'un joueur perd il est eliminé, ainsi il restera dans la liste et quand son tour viendra son tour passera automatiquement"""
    def changePlayer(self, joueur):
        #On considère que le joueur termine son tour s'il le passe (en cliquant sur un bouton) ou si son nombre d'actions maximal est atteint.
        if joueur.actions == 0 or joueur.passe == True :

            #Ce n'est plus au joueur de joué son tour
            joueur.actions = 3
            joueur.passe = False
            joueur.playing = False
            #en fonction de son positionnement, il laisse la place à tel ou tel autre joueur

            numberOfPlayers = len(self.listeJoueur)

            if joueur.number == 1 :
                for i in range (0, len(self.listeJoueur)):
                    #On passe la main au deuxième joueur
                    if self.listeJoueur[i].number == 2 and self.listeJoueur[i].deleted == False :
                        self.listeJoueur[i].playing = True
                        return
                    # si le joueur 2 est mort on passe son tour
                    elif self.listeJoueur[i].number == 2 and self.listeJoueur[i].deleted == True :
                        self.listeJoueur[i].passe = True
                        self.changePlayer(self.listeJoueur[i])

            if joueur.number == 2 :
                for i in range (0, len(self.listeJoueur)):
                    #On passe la main au troisième joueur
                    if self.listeJoueur[i].number == 3 and self.listeJoueur[i].deleted == False and numberOfPlayers >= 3:
                        self.listeJoueur[i].playing = True
                        return
                    #si le joueur 3 est mort on passe son tour
                    elif self.listeJoueur[i].number == 3 and self.listeJoueur[i].deleted == True and numberOfPlayers >= 3:
                        self.listeJoueur[i].passe = True
                        self.changePlayer(self.listeJoueur[i])
                    # S'il y en a pas on passe la main au premier joueur
                    elif self.listeJoueur[i].number == 1 and numberOfPlayers <= 2 :
                        self.listeJoueur[i].playing = True
                        return


            if joueur.number == 3 and numberOfPlayers >= 3 :
                for i in range (0, len(self.listeJoueur)):
                    #On passe la main au quatrième joueur
                    if self.listeJoueur[i].number == 4 :
                        self.listeJoueur[i].playing = True
                        return
                    # si le joueur 4 est mort on passe son tour
                    elif self.listeJoueur[i].number == 4 and self.listeJoueur[i].deleted == True and numberOfPlayers >= 3:
                        self.listeJoueur[i].passe = True
                        self.changePlayer(self.listeJoueur[i])
                    #S'il n'y en a pas on passe la main au premier joueur
                    elif self.listeJoueur[i].number == 1 and numberOfPlayers <= 3 :
                        self.listeJoueur[i].playing = True
                        return
                    # si le joueur 1 est mort on passe son tour
                    elif self.listeJoueur[i].number == 1 and self.listeJoueur[i].deleted == True and numberOfPlayers >= 3:
                        self.listeJoueur[i].passe = True
                        self.changePlayer(self.listeJoueur[i])

            if joueur.number == 4 and numberOfPlayers >= 4 :
                for i in range (0, len(self.listeJoueur)):
                    #On passe la main au premier joueur
                    if self.listeJoueur[i].number == 1 :
                        self.listeJoueur[i].playing = True
                        return
                    # si le joueur 1 est mort on passe son tour
                    elif self.listeJoueur[i].number == 1 and self.listeJoueur[i].deleted == True and numberOfPlayers >= 3:
                        self.listeJoueur[i].passe = True
                        self.changePlayer(self.listeJoueur[i])
        return False


