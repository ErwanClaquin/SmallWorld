from Unite import *
from DataName import *

class Humans(Unite):
    def __init__(self):
        super().__init__()
        self.number = 6
        self.race = nameHumans

    def Power(self):
        #Todo : attribuer un pouvoir de classe
        return