from random import *
class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character,Fantassin,Bretteur,Chevalier,nbPixelX,index):
        
        self.plateauDeJeu = plateauDeJeu
        self.nbPixelX = nbPixelX
        self.Index = index
        self.Character = Character
        self.Fantassin = Fantassin
        self.Bretteur = Bretteur
        self.Chevalier = Chevalier
        
        self.personnage = Chevalier('blue',plateauDeJeu,nbPixelX,"personnage",index)
        self.personnage4 = Chevalier('blue',plateauDeJeu,nbPixelX,"personnage4",index)
        

        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[20][2] = self.personnage
        self.plateauDeJeu.tableauGeneral[22][2] = self.personnage4
        
        

        self.personnage.setPosition(self.plateauDeJeu.tableauGeneral[20][0])
        self.personnage4.setPosition(self.plateauDeJeu.tableauGeneral[22][0]) 
        

        self.initArmeeRouge()
    
         
        
       
    def initArmeeRouge(self):

        stop = 0
        tableau = []
        while stop == 0:
            
            soldatPersonnage =int(input("Combien de Fantassin est composée de l'equipe énemies !"))

            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Fantassin("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)
                    
            soldatPersonnage =int(input("Combien de Bretteur est composée de l'equipe énemies !"))
            
            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Bretteur("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)

            soldatPersonnage =int(input("Combien de Chevalier est composée de l'equipe énemies !"))
            
            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Chevalier("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)
                    shuffle(tableau)
                print(tableau)
            
            for x in range(0,len(tableau)):
                    self.plateauDeJeu.tableauGeneral[x][2] = tableau[x]
                    
            for y in range(0,len(tableau)):
                tableau[y].setPosition(self.plateauDeJeu.tableauGeneral[y][0])
                    
            break
              
        
        
        
    
