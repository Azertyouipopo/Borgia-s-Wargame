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
    
    def __init__(self,color,plateauDeJeu,nbPixelX,name,index):
        self.Index = index
        self.name = name 
        self.plateauDeJeu = plateauDeJeu
        self.role = "Personnage"
        self.tabStatAlgo = []
        self.initiative = 80
        self.identificateur = id(self) # Inscript l'id de lobjet 
        self.lifePts = 50
        self.speed = 1
        self.armor = 5
        self.strengh = 10
        self.actionPts = 1
        self.xOry = nbPixelX
        self.couleur = color
        self.putInArmy(self,color)
     
    
        


    ########################### Seter #############################


    #Fonction static qui rentre chaque object instancier
    #deux tableau red et blue représentent les deux equipe
    
    @staticmethod 
    def putInArmy(self,color):
        if color == 'blue': 
            self.blue.append(self)#Insert l'objet dans le tableau
        else:
            self.red.append(self)
            
    @staticmethod    
    def destroyArmy(self):
        Character.blue = []
        Character.red = []
        

    @staticmethod   
    def setDegatRecuTotal(self,value):
        self.degatRecuTotal += value
        

    
    
    @staticmethod   
    def getDegatRecuTotal():
        return degatRecuTotal 
        
        
        

    def setPosition(self,valueInt):
        self.position = valueInt
        



            
    
    #Fonction qui gére le deplacement de l'objet 
    def setMouvement(self):

        
        
        objPersonnage ="obj"
        enemieNear,objPersonnage = self.verifEnemieNear()
        
        if enemieNear == 1:
            
            mouvement = randrange(1,5,1)# Genere un nb aleatoire pour le deplacement
            valeurBloquer = self.verifBloquerCharacter(mouvement)
            
            compteur= 0
            

            
            if valeurBloquer == 0:
                
                valeurDeVerif = self.verifCharacterNear(mouvement)
                
                
                if valeurDeVerif == 1:
                
                 # Nous recherchons la position de notre personage et la remplaçon par une case vide 
                    for i in self.plateauDeJeu.tableauGeneral :
                        
                        verificationPresence = 0
                        
                        if self.plateauDeJeu.tableauGeneral[compteur][0] == self.position:
                            
                            self.setPosition(self.newPosition)             
                            temp = self.plateauDeJeu.tableauGeneral[compteur][2]
                            self.plateauDeJeu.tableauGeneral[compteur][2] = "vide"
                            break

                        
                        compteur += 1

                    
                    creatNewPosition = 0
                    indice = 0

                    #Nous recherchons un la nouvelle position et nous remplaçon la case vide par l'objet 
                    while creatNewPosition != 1 :
                        
                        if self.plateauDeJeu.tableauGeneral[indice][0] == self.newPosition :
                            self.plateauDeJeu.tableauGeneral[indice][2] = temp
                            
                            
                            break
                        indice = indice + 1

                    return 1 # Représente le remplacement de la case vide et de l'objet 
                            
        if enemieNear == 0 and objPersonnage != 0 :
             vieOrMort = self.attaqueCible (objPersonnage)
             #print("ZEFdqsqqqqqqqqqqqqqqqqqqqq")
             return vieOrMort #Représente si en vie ou mort 

        return "erreur"
             
             #Fonction qui inflige des dégats à une cible proche
    def attaqueCible (self,objPersonnage):
        attaquePossible = randrange(1,101,1)
        if  attaquePossible <= self.initiative:
           vieOrMort = objPersonnage.degatSubit(self.strengh)
           if self.couleur == "blue":
               self.degatInfligeTotal += self.strengh
               
           return vieOrMort

        #Cette fonction est pour retiré des points de vie à une unité en fonction de l'attaque reçu
        
    def degatSubit(self,strengh):

        if self.lifePts <= 0 :
           self.Index.mort(self)
           return "mort"

        if self.armor > 0 and self.lifePts > 0:
            degatTampon =  strengh*(self.armor / 100)
            if self.couleur == "blue":
                value = strengh - degatTampon
                self.setDegatRecuTotal(self,value)
            
            
            self.lifePts = self.lifePts -(strengh - degatTampon)
            self.armor = self.armor - 1           
            return 1 
        
        if self.lifePts > 0  and self.armor <= 0:
            if self.couleur == "blue":
                self.setDegatRecuTotal(self,self.strengh)
            self.lifePts = self.lifePts - strengh
            #print(self.lifePts," vie ")
            return "vie"

        
        if self.lifePts <= 0 :
            self.Index.mort(self)
            return "mort"
    

        
                
        #verifEnemienear est ici pour tester s'il y a des ennemies sur chaque case adjacente à celle de l'unité sélectionnée
    def verifEnemieNear(self):
        #4
        newCoordone = self.position[1] - 10
        newCoordoneForward = [self.position[0], newCoordone]
        compteur = 0 
        for i in self.plateauDeJeu.tableauGeneral:
            
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == newCoordoneForward :
               if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide" :
                   objPersonnage = self.plateauDeJeu.tableauGeneral[compteur][2]
                   if objPersonnage.couleur != self.couleur :
                       return 0,objPersonnage
                    
                
            compteur += 1
        #1    
        newCoordone = self.position[1] + 10
        newCoordoneBack = [self.position[0], newCoordone]
        compteur = 0 
        for i in self.plateauDeJeu.tableauGeneral:
            
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == newCoordoneBack :
                if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide" :
                    objPersonnage = self.plateauDeJeu.tableauGeneral[compteur][2]
                    if objPersonnage.couleur != self.couleur :
                        return 0,objPersonnage

                
            compteur += 1
        #2    
        newCoordone = self.position[0] - 10
        newCoordoneLeft = [newCoordone,self.position[1]]
        compteur = 0 
        for i in self.plateauDeJeu.tableauGeneral:
            
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == newCoordoneLeft :
                if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide" :
                    objPersonnage = self.plateauDeJeu.tableauGeneral[compteur][2]
                    if objPersonnage.couleur != self.couleur :
                        return 0,objPersonnage

                
            compteur += 1
        
        return 1,0

        #3
        newCoordone = self.position[0] + 10
        newCoordoneRight = [newCoordone,self.position[1]]
        compteur = 0 
        for i in self.plateauDeJeu.tableauGeneral:
            
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == newCoordoneRight :
                if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide" :
                    objPersonnage = self.plateauDeJeu.tableauGeneral[compteur][2]
                    if objPersonnage.couleur != self.couleur :
                        return 0,objPersonnage

                
            compteur += 1
        
        return 1,0
        
        
    def verifBloquerCharacter(self,mouvement):
    
        
        if mouvement == 1 :
            
            if self.position[1] != 10:
                
                return 0
            

            else :
                return 1
            
    
        if mouvement == 2 :
            
            if self.position[0] != 10:
                
                return 0

            else :
                return 1
            
        if mouvement == 3 :
            
            if self.position[0] != self.xOry:
                
                return 0

            else :
                return 1
        
        if mouvement == 4 :
            
            if self.position[1] != self.xOry:
                
                return 0

            else :
                return 1
            
            

   


                    
                    
    def verifCharacterNear(self,mouvement):
        if mouvement == 1 :
            
            newCoordone =self.position[1] - 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [self.position[0], newCoordone] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0
                compteur +=1

        if mouvement == 2 :
            
            newCoordone =self.position[0] - 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [newCoordone,self.position[1]] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0
                compteur +=1

        if mouvement == 3 :
            
            newCoordone =self.position[0] + 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [newCoordone,self.position[1]] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0
                compteur +=1

        if mouvement == 4 :
            newCoordone =self.position[1] + 10  # si 4 alors  [x, y + 10] 
            self.newPosition = [self.position[0], newCoordone] # Nous donnons la news position à l'objet
            compteur = 0
          
            for i in self.plateauDeJeu.tableauGeneral:
                
                if  self.plateauDeJeu.tableauGeneral[compteur][0] == self.newPosition :
                    if self.plateauDeJeu.tableauGeneral[compteur][2] == "vide":
                        return 1
                    if self.plateauDeJeu.tableauGeneral[compteur][2] != "vide":
                        return 0
                compteur +=1
                

####################################################################################################################################################################
###################################################################### Class Fantassin #############################################################################
####################################################################################################################################################################
    
class Fantassin(Character):

    degatRecuTotal = 0
    degatInfligeTotal = 0
    
    def __init__(self,color,plateauDeJeu,nbPixelX,name,index):
        Character.__init__(self,color,plateauDeJeu,nbPixelX,name,index)
        self.role = "Fantassin"    
        self.initiative = 60           # L'initiative est à changer en fonction des perso
        self.lifePts = 60
        self.armor = 10
        self.strengh = 15
        self.cost = 15
        
    def getVariableAlgo(self):
        return self.degatRecuTotal,self.degatInfligeTotal

    def attaqueCible (self,objPersonnage):
        attaquePossible = randrange(1,101,1)
        if  attaquePossible <= self.initiative:
           vieOrMort = objPersonnage.degatSubit(self.strengh)
           if self.couleur == "blue":
               Fantassin.degatInfligeTotal += self.strengh
               
           return vieOrMort

        #Cette fonction est pour retiré des points de vie à une unité en fonction de l'attaque reçu
        
    def degatSubit(self,strengh):

        if self.lifePts <= 0 :
           self.Index.mort(self)
           return "mort"

        if self.armor > 0 and self.lifePts > 0:
            degatTampon =  strengh*(self.armor / 100)
            if self.couleur == "blue":
                value = strengh - degatTampon
                Fantassin.degatRecuTotal += value
            
            
            self.lifePts = self.lifePts -(strengh - degatTampon)
            self.armor = self.armor - 1           
            return 1 
        
        if self.lifePts > 0  and self.armor <= 0:
            if self.couleur == "blue":
                Fantassin.degatRecuTotal += strengh
            self.lifePts = self.lifePts - strengh
            #print(self.lifePts," vie ")
            return "vie"

        
        if self.lifePts <= 0 :
            self.Index.mort(self)
            return "mort"

    


####################################################################################################################################################################
###################################################################### Class Bretteur  #############################################################################
####################################################################################################################################################################
        
class Bretteur(Character):
    degatRecuTotal = 0
    degatInfligeTotal = 0
    
    def __init__(self,color,plateauDeJeu,nbPixelX,name,index):
        Character.__init__(self,color,plateauDeJeu,nbPixelX,name,index)
        self.role = "Bretteur"
        self.initiative = 75           # L'initiative est à changer en fonction des perso
        self.lifePts = 60
        self.armor = 2
        self.strengh = 20
        self.cost = 20

    def getVariableAlgo(self):
        return self.degatRecuTotal,self.degatInfligeTotal

    def attaqueCible (self,objPersonnage):
        attaquePossible = randrange(1,101,1)
        if  attaquePossible <= self.initiative:
           vieOrMort = objPersonnage.degatSubit(self.strengh)
           if self.couleur == "blue":
               Bretteur.degatInfligeTotal += self.strengh
               
           return vieOrMort

        #Cette fonction est pour retiré des points de vie à une unité en fonction de l'attaque reçu
        
    def degatSubit(self,strengh):

        if self.lifePts <= 0 :
           self.Index.mort(self)
           return "mort"

        if self.armor > 0 and self.lifePts > 0:
            degatTampon =  strengh*(self.armor / 100)
            if self.couleur == "blue":
                value = strengh - degatTampon
                Bretteur.degatRecuTotal += value
            
            
            self.lifePts = self.lifePts -(strengh - degatTampon)
            self.armor = self.armor - 1           
            return 1 
        
        if self.lifePts > 0  and self.armor <= 0:
            if self.couleur == "blue":
                Bretteur.degatRecuTotal += strengh
            self.lifePts = self.lifePts - strengh
            #print(self.lifePts," vie ")
            return "vie"

        
        if self.lifePts <= 0 :
            self.Index.mort(self)
            return "mort"



####################################################################################################################################################################
###################################################################### Class Chevalier #############################################################################
####################################################################################################################################################################
        
class Chevalier(Character):
    degatRecuTotal = 0
    degatInfligeTotal = 0
    def __init__(self,color,plateauDeJeu,nbPixelX,name,index):
        Character.__init__(self,color,plateauDeJeu,nbPixelX,name,index)
        self.role = "Chevalier"
        self.initiative = 65           # L'initiative est à changer en fonction des perso
        self.lifePts = 75
        self.armor = 15
        self.strengh = 25
        self.cost = 35

    def getVariableAlgo(self):
        return self.degatRecuTotal,self.degatInfligeTotal

    def attaqueCible (self,objPersonnage):
        attaquePossible = randrange(1,101,1)
        if  attaquePossible <= self.initiative:
           vieOrMort = objPersonnage.degatSubit(self.strengh)
           if self.couleur == "blue":
               Chevalier.degatInfligeTotal += self.strengh
               
           return vieOrMort

        #Cette fonction est pour retiré des points de vie à une unité en fonction de l'attaque reçu
        
    def degatSubit(self,strengh):

        if self.lifePts <= 0 :
           self.Index.mort(self)
           return "mort"

        if self.armor > 0 and self.lifePts > 0:
            degatTampon =  strengh*(self.armor / 100)
            if self.couleur == "blue":
                value = strengh - degatTampon
                Chevalier.degatRecuTotal += value
            
            
            self.lifePts = self.lifePts -(strengh - degatTampon)
            self.armor = self.armor - 1           
            return 1 
        
        if self.lifePts > 0  and self.armor <= 0:
            if self.couleur == "blue":
                Chevalier.degatRecuTotal += strengh
            self.lifePts = self.lifePts - strengh
            #print(self.lifePts," vie ")
            return "vie"

        
        if self.lifePts <= 0 :
            self.Index.mort(self)
            return "mort"
        
    



####################################################################################################################################################################
###################################################################### Class Fantassin #############################################################################
####################################################################################################################################################################
        
class Archer(Character):
    def __init__(self,color,plateauDeJeu,nbPixelX,name,index):
        super().__init__(self,color,plateauDeJeu,nbPixelX,name,index)
        self.Index = index
        self.name = name 
        self.plateauDeJeu = plateauDeJeu
        self.role = "Personnage"
        self.initiative =  65          # L'initiative est à changer en fonction des perso
        self.identificateur = id(self) # Inscript l'id de lobjet 
        self.lifePts = 5
        self.armor = 0
        self.strengh = 2


