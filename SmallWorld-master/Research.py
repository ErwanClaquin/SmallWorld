from Cases import *


def searchUniteOnCase(army, listeCase):
    listeUnite = []
    for element in army:
        for case in listeCase:
            if element in case:
                print("Armée trouvée !")
                return True
    return False


def searchWhichCaseOn(x, y):
    i = 0
    for case in listeCase:
        if case.onCase(x, y):
            print("vous êtes sur la case", listeCase[i])
        i += 1
