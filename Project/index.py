from Package.soldier import*
from tkinter import *
from random import *

class Index:

    verif = 0 
    
    def __init__ (self) :
        
        ### Initialisation des attribut lambda ###
        self.nbPixelX = 50
        self.nbPixelY = 50
        self.indiceB = 0
        self.indiceR = 0
        self.step = 10

        
        ###Initialisation des classes ###
        self.plateauDeJeu = Plateau(self.nbPixelX,self.nbPixelY,self.step) # Instancie notre plateauDejeu
        self.trya = Position(self.plateauDeJeu,Character,self.nbPixelX,self) # implante des soldat dans le terain
        self.tableauBleu = Character.blue #Recuperation du tableau bleu représentant une equipe
        self.tableauRed = Character.red #Recuperation du tableau bleu représentant une equipe
        
        self.gestionDePartie ()



    def view(self,plateauDeJeu):
        
        self.plateauDeJeu.formatViewArray(2) # Tableau Character
        print("")
        #self.plateauDeJeu.formatViewArray(1) #Tableau Terrain
        print("")
        #self.plateauDeJeu.formatViewArray(0) #Tableau Coordonees
        print("")
        self.plateauDeJeu.formatViewArrayGeneral() #TableauGeneral




    def mouvement(self):

        if len(self.tableauRed) >= len(self.tableauBleu):
            tailleMax = len(self.tableauRed) - 1
            
            for x in range(0,len(self.tableauRed)):
                
                tailleMax = len(self.tableauRed) - 1
                
                if x <= len(self.tableauBleu) - 1 :

                    vieOrMort = self.tableauBleu[x].setMouvement()
                    
                if x <= tailleMax:    
                    self.tableauRed[x].setMouvement()
                    
                           

        
    #Fonction  gére la gestion globale de notre application 
    def gestionDePartie (self):
        
        tempsDeplacement = 50
        self.view(self.plateauDeJeu)
        
        for i in range (0, tempsDeplacement):
            
            self.mouvement()
            self.view(self.plateauDeJeu) #appéle de notre fonction d'affichage
            
               
    
    def mort(self,PersonnageMort):
        compteur = 0

        for i in self.plateauDeJeu.tableauGeneral:
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == PersonnageMort.position :
                self.plateauDeJeu.tableauGeneral[compteur][2] = "vide"
            compteur +=1

            
        if PersonnageMort.couleur == "red":
            for i in range(0,len(self.tableauRed)):
                print(i)
                if self.tableauRed[i] == PersonnageMort:
                    del self.tableauRed[i]
                    break
                    
        if PersonnageMort.couleur == "blue":
            for i in range(0,len(self.tableauBleu)):
                if self.tableauBleu[i] == PersonnageMort:
                    print("Suppresion d'un joeur d'equipe bleu ")
                    del self.tableauBleu[i]
                    break
        

    


objzqsed = Index()

    


