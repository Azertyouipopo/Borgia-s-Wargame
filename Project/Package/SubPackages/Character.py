
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

    ########################### Constructeur  #############################
    
    def __init__(self,color):
        
        self.role = "Personnage"
        self.identificateur = id(self) # Inscript l'id de lobjet 
        self.lifePts = 50
        self.speed = 1
        self.armor = 5
        self.strengh = 10
        self.actionPts = 1
        self.putInArmy(self,'blue')
        


    ########################### Seter #############################


    #Fonction static qui rentre chaque object instancier
    #deux tableau red et blue représentent les deux equipe
    
    @staticmethod 
    def putInArmy(self,color):
        if color == 'blue': 
            self.blue.append(self)#Insert l'objet dans le tableau

            
    # Fonction qui insére ces coordonée de postion d'apres le tableauGeneral
    def setPosition(self,tab):   
        self.oldPosition = tab 
        print(self.oldPosition)

    #Fonction qui gére le deplacement de l'objet 
    def setMouvement(self):
        mouvement = randrange(1,5,1)
        print(self.oldPosition)
        print(mouvement)
        
