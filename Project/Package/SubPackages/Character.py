
from random import *

class Character:
    
##     Classe définissant une personne caractérisée par :
##    - son role ;
##    - ça vie ;
##    - ça vitesse
##    - son armure
##    - force
##    - ça position

    blue = [] #Creation d'une equipe soit equipe bleu
    red = []#Creation d'une equipe soit equipe rouge
    
    def __init__(self,color):
        self.role = "Personnage"
        self.identificateur = id(self) # Inscript l'id de lobjet 
        self.lifePts = 50
        self.speed = 1
        self.armor = 5
        self.strengh = 10
        self.actionPts = 1

        self.putInArmy('blue',id(self))
    
    def putInArmy(cls,color,identificateur):
        if color == 'blue': 
            cls.blue.append(identificateur)

    def setPosition(self,tab): # Defini d   
        self.oldPosition = tab
        print(self.oldPosition)
