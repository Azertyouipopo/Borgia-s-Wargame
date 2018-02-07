from Package.soldier import*
from tkinter import *
from random import *

class Index:

    verif = 0 
    
    def __init__ (self) :

        self.plateauDeJeuTK = PlateauDeJeuTK()
        
        ### Initialisation des attribut lambda ###
        self.nbPixelX = self.plateauDeJeuTK.totalCaseTK
        self.nbPixelY = self.plateauDeJeuTK.totalCaseTK
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
        
        #self.plateauDeJeu.formatViewArray(2) # Tableau Character
        print("")
        #self.plateauDeJeu.formatViewArray(1) #Tableau Terrain
        print("")
        #self.plateauDeJeu.formatViewArray(0) #Tableau Coordonees
        print("")
        #self.plateauDeJeu.formatViewArrayGeneral() #TableauGeneral

    def conditionFinDePartie(self):
        nombreMortRouge = 0
        nombreMortBleu = 0
        for x in range(0,len(self.tableauRed)):
            
            if self.tableauRed[x] == "mort":
                nombreMortRouge += 1

            if self.tableauBleu[x] == "mort":
                nombreMortBleu += 1
                
        if nombreMortRouge == len(self.tableauRed):
            return 1

        if nombreMortBleu == len(self.tableauBleu):
            return 1

        return 0 
        


    def mouvement(self):

        if len(self.tableauRed) >= len(self.tableauBleu):
            
            tailleMax = len(self.tableauRed) - 1
            
            for x in range(0,len(self.tableauRed)):

               
                
                tailleMax = len(self.tableauRed) - 1
                
                if x <= len(self.tableauBleu) - 1 :
                    if self.tableauBleu[x] != "mort":
                        vieOrMort = self.tableauBleu[x].setMouvement()
                        self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
                        #self.plateauDeJeuTK.positionJoueurBleu(self.tableauBleu)
                if x <= tailleMax:
                    if self.tableauRed[x] != "mort":
                        self.tableauRed[x].setMouvement()
                        self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
                        #self.plateauDeJeuTK.positionJoueurRouge(self.tableauRed)
                           

        
    #Fonction  gére la gestion globale de notre application 
    def gestionDePartie (self):
        
        tempsDeplacement = 300
        self.view(self.plateauDeJeu)

        
        
        for i in range (0, tempsDeplacement):
            
            
            self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
            self.mouvement()
            self.view(self.plateauDeJeu) #appéle de notre fonction d'affichage

            variableFinPartie = self.conditionFinDePartie()

            if variableFinPartie == 1 :
                print("fin dE PARTIE")
                break
        print(self.tableauBleu)
        print(self.tableauRed)
    
        
               
    
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
                    self.tableauRed[i] = "mort"
                    print(self.tableauRed,"Jouer rouge mort")
                    break
                    
        if PersonnageMort.couleur == "blue":
            for i in range(0,len(self.tableauBleu)):
                if self.tableauBleu[i] == PersonnageMort:
                    self.tableauBleu[i] = "mort"
                    print(self.tableauBleu,"Jouer bleu mort")
                    break
        

    


objzqsed = Index()

    


