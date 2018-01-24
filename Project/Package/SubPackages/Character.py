
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
    
    def __init__(self,color,plateauDeJeu):

        self.plateauDeJeu = plateauDeJeu
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

    def position(self,valueInt):
        self.position = valueInt
        
            
    
    #Fonction qui gére le deplacement de l'objet 
    def setMouvement(self):
        mouvement = randrange(1,5,1)
        print(mouvement)
        if mouvement == 4 or mouvement == 3:
            donne =self.position[1] + 10
            self.newPosition = [self.position[0], donne]

            for i in self.plateauDeJeu.tableauGeneral :
                if self.plateauDeJeu.tableauGeneral[2][0] == self.position :
                    self.plateauDeJeu.tableauGeneral[2][2] = "vide"
            creatNewPosition = 0
            indice = 0 
            while creatNewPosition != 1 :
                if self.plateauDeJeu.tableauGeneral[indice][0] == self.newPosition :
                    self.plateauDeJeu.tableauGeneral[indice][2] == self.self
                    break
                indice = indice + 1
                
                    
            
        
        
        
