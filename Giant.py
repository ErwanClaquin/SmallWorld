from Unite import *
from DataName import *

class Giant(Unite):
    def __init__(self):
        super().__init__()
        self.number = 6
        self.race = nameGiant

    def Power(self):
        #Todo : attribuer un pouvoir de classe
        return