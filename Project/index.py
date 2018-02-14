from Package.soldier import*
from tkinter import *
from random import *
import time

class Index:

    verif = 0 
    
    def __init__ (self) :

        
        #self.plateauDeJeuTK = PlateauDeJeuTK() # Initialisation du plateauTkinter
        print("bug")

        ### Initialisation des attribut lambda ###
        #self.nbPixelX = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour x
        self.nbPixelX = 100
        self.nbPixelY = 100
        #self.nbPixelY = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour y
        self.indiceB = 0 # Initialisation d'un indice de recherche in array Bleu
        self.indiceR = 0 # Initialisation d'un indice de recherche in array Rouge
        self.step = 10 # variable de controle 

        
        ###Initialisation des classes ###
        self.plateauDeJeu = Plateau(self.nbPixelX,self.nbPixelY,self.step) # Instancie notre plateauDejeu
        
        self.trya = Position(self.plateauDeJeu,Character,Fantassin,Bretteur,Chevalier,self.nbPixelX,self) # implante des soldat dans le terain
        self.tableauBleu = Character.blue #Recuperation du tableau bleu représentant une equipe
        self.tableauRed = Character.red #Recuperation du tableau bleu représentant une equipe

        #Une fois que les attribut sont initialiser la partie commance !
        
        self.gestionDePartie () # apppéle  de la fonction de gestion de partie 



    def view(self,plateauDeJeu):
        pass   
        #self.plateauDeJeu.formatViewArray(2) # Tableau Character
        #print("")
        #self.plateauDeJeu.formatViewArray(1) #Tableau Terrain
        #print("")
        #self.plateauDeJeu.formatViewArray(0) #Tableau Coordonees
        #print("")
        #self.plateauDeJeu.formatViewArrayGeneral() #TableauGeneral


    # Note fonction va déterminer si tous les joeur d'une equipe est mort
    ## ou pas si c'est le cas la partie est fini
    
    def conditionFinDePartie(self):
        
        nombreMortRouge = 0 # var int représentant le nombre de mort de l'equipe Rouge
        nombreMortBleu = 0 # var int représentant le nombre de mort de l'equipe Bleu

        #Boucle qui parcoure les tableau red,bleu 
        for x in range(0,len(self.tableauRed)):

            # si un indice du tableauRed alors incrémentation de la variable 
            if self.tableauRed[x] == "mort":
                nombreMortRouge += 1

            # si un indice du tableauBleu alors incrémentation de la variable 
            
        #si le nombre de mort est égale au nombre de joeur alors toutes l'equipe est morte !        
        if nombreMortRouge == len(self.tableauRed):
            return 1 # 1 veut dire equipe bleu gagnante !

        
        for y in range(0,len(self.tableauBleu)):        

            if self.tableauBleu[y] == "mort":
                    nombreMortBleu += 1

        
        #si le nombre de mort est égale au nombre de joeur alors toutes l'equipe est morte !
        if nombreMortBleu == len(self.tableauBleu):
            return 2 # 2 represente l'equipe rouge gagnante
        
        return 0 
        

    # fonction qui gére le deplacement des unités 
    def mouvement(self):

        # Verificaion quelle equipe est plus grande de l'autre
        if len(self.tableauRed) >= len(self.tableauBleu):

            
            tailleMax = len(self.tableauRed) - 1 #var type int , contien la taille tu tableauRed
            
            for x in range(0,len(self.tableauRed)):

               
                tailleMax = len(self.tableauRed) - 1
                
                if x <= len(self.tableauBleu) - 1 :
                    if self.tableauBleu[x] != "mort":
                        vieOrMort = self.tableauBleu[x].setMouvement()
                        #self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
                        #self.plateauDeJeuTK.positionJoueurBleu(self.tableauBleu)
                if x <= tailleMax:
                    if self.tableauRed[x] != "mort":
                        self.tableauRed[x].setMouvement()
                        #self.plateauDeJeuTK.setTabCharacterRouge(self.plateauDeJeu.getTableauGeneral(),self.tableauRed)
                        #self.plateauDeJeuTK.positionJoueurRouge(self.tableauRed)

    def remisAzero(self):

        Character.blue = []#Destruction du tableau precedent
        Character.red = [] #Destruction du tableau precedent       
        #self.nbPixelX = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour x
        self.nbPixelX = 100
        self.nbPixelY = 100
        #self.nbPixelY = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour y
        self.indiceB = 0 # Initialisation d'un indice de recherche in array Bleu
        self.indiceR = 0 # Initialisation d'un indice de recherche in array Rouge
        self.step = 10 # variable de controle 
        ###Initialisation des classes ###
        self.plateauDeJeu = Plateau(self.nbPixelX,self.nbPixelY,self.step) # Instancie notre plateauDejeu
        
        self.trya = Position(self.plateauDeJeu,Character,Fantassin,Bretteur,Chevalier,self.nbPixelX,self) # implante des soldat dans le terain
        self.tableauBleu = Character.blue #Recuperation du tableau bleu représentant une equipe
        self.tableauRed = Character.red #Recuperation du tableau bleu représentant une equipe
        self.gestionDePartie()

        
    #Fonction  gére la gestion globale de notre application 
    def gestionDePartie (self):
        
        tempsDeplacement = 0
        self.view(self.plateauDeJeu)
        fin = 1
        #self.plateauDeJeuTK.setTabCharacterRouge(self.plateauDeJeu.getTableauGeneral(),self.tableauRed)

        
        while  fin ==  1:
            
            tempsDeplacement += 1

            #self.plateauDeJeuTK.setTabCharacterRouge(self.plateauDeJeu.getTableauGeneral(),self.tableauRed)

            self.mouvement()
            self.view(self.plateauDeJeu) #appéle de notre fonction d'affichage
            variableFinPartie = self.conditionFinDePartie()
            #self.plateauDeJeuTK.setTabCharacterRouge(self.plateauDeJeu.getTableauGeneral(),self.tableauRed)

            if variableFinPartie == 1 :
                print(self.tableauBleu,"Tableau de l'equipe bleu ")
                print(self.tableauRed,"Tableau de l'equipe rouge")
                print(tempsDeplacement)
                print("L'equipe bleu à gagner !")
                self.remisAzero()
                break

            
            if variableFinPartie == 2 :
                print(self.tableauBleu,"Tableau de l'equipe bleu ")
                print(self.tableauRed,"Tableau de l'equipe rouge")
                print(tempsDeplacement)
                print("L'equipe rouge à gagner !")
                self.remisAzero()
                break
        
    
        
               
    
    def mort(self,PersonnageMort):
        compteur = 0

        for i in self.plateauDeJeu.tableauGeneral:
            if  self.plateauDeJeu.tableauGeneral[compteur][0] == PersonnageMort.position :
                self.plateauDeJeu.tableauGeneral[compteur][2] = "vide"
            compteur +=1

            
        if PersonnageMort.couleur == "red":
            for i in range(0,len(self.tableauRed)):
                
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

    


