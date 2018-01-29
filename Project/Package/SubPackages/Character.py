
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
        mouvement = randrange(1,5,1)# Genere un nb aleatoire pour le deplacement
        print(mouvement)
        compteur= 0

  

        valeurDeVerif = self.verifCharacterNear(mouvement)
        if valeurDeVerif == 1:
        
         # Nous recherchons la position de notre personage et la remplaçon par une case vide 
            for i in self.plateauDeJeu.tableauGeneral :
                compteur += 1
                verificationPresence = 0

                if self.plateauDeJeu.tableauGeneral[compteur][0] == self.position:
                    self.position = self.newPosition              
                    temp = self.plateauDeJeu.tableauGeneral[compteur][2]
                    self.plateauDeJeu.tableauGeneral[compteur][2] = "vide"
                    break

            
            creatNewPosition = 0
            indice = 0

            #Nous recherchons un la nouvelle position et nous remplaçon la case vide par l'objet 
            while creatNewPosition != 1 :
                if self.plateauDeJeu.tableauGeneral[indice][0] == self.newPosition :
                    self.plateauDeJeu.tableauGeneral[indice][2] = temp
                    print(self.position)
                    break
                indice = indice + 1
        
        

                    
                    
    def verifCharacterNear(self,mouvement):
        if mouvement == 1 :
            
            newCoordone =self.position[1] - 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [self.position[0], newCoordone] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                compteur +=1
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0

        if mouvement == 2 :
            
            newCoordone =self.position[0] - 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [newCoordone,self.position[1]] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                compteur +=1
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0

        if mouvement == 3 :
            
            newCoordone =self.position[0] + 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [newCoordone,self.position[1]] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                compteur +=1
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0

        if mouvement == 4 :
            newCoordone =self.position[1] + 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [self.position[0], newCoordone] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                compteur +=1
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0
                
            
        
        
        
