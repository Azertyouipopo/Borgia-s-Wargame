
from random import *

class Character:
    
##     Classe définissant une personne caractérisée par :
##    - son role ;
##    - ça vie ;
##    - ça vitesse
##    - son armure
##    - force
##    - ça position

    def __init__(self):
        self.role = "Personnage"
        self.lifePts = 50
        self.speed = 1
        self.armor = 5
        self.strengh = 10
        self.actionPts = 1
        

    def deplacement(self):
        mouvement = randrange(1,5,1)
        if mouvement == 1:
            self.oldPosition[1] = self.oldPosition[1] - 10
            print(self.oldPosition)
        

    def setPosition(self,tab):
        self.oldPosition = tab
        print(self.oldPosition)
