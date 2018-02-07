from Package.soldier import*
from tkinter import *
from random import *

class Index:

    verif = 0 
    
    def __init__ (self) :

        self.plateauDeJeuTK = PlateauDeJeuTK() # Initialisation du plateauTkinter
        
        ### Initialisation des attribut lambda ###
        self.nbPixelX = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour x
        self.nbPixelY = self.plateauDeJeuTK.totalCaseTK # recuperation d'apres obj pDJTK des case pour y
        self.indiceB = 0 # Initialisation d'un indice de recherche in array Bleu
        self.indiceR = 0 # Initialisation d'un indice de recherche in array Rouge
        self.step = 10 # variable de controle 

        
        ###Initialisation des classes ###
        self.plateauDeJeu = Plateau(self.nbPixelX,self.nbPixelY,self.step) # Instancie notre plateauDejeu
        self.trya = Position(self.plateauDeJeu,Character,self.nbPixelX,self) # implante des soldat dans le terain
        self.tableauBleu = Character.blue #Recuperation du tableau bleu représentant une equipe
        self.tableauRed = Character.red #Recuperation du tableau bleu représentant une equipe

        #Une fois que les attribut sont initialiser la partie commance !
        
        self.gestionDePartie () # apppéle  de la fonction de gestion de partie 



    def view(self,plateauDeJeu):
           """ddd""" 
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
            if self.tableauBleu[x] == "mort":
                nombreMortBleu += 1

        #si le nombre de mort est égale au nombre de joeur alors toutes l'equipe est morte !        
        if nombreMortRouge == len(self.tableauRed):
            return 1
        
        #si le nombre de mort est égale au nombre de joeur alors toutes l'equipe est morte ! 
        if nombreMortBleu == len(self.tableauBleu):
            return 1
        
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
                        self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
                        #self.plateauDeJeuTK.positionJoueurBleu(self.tableauBleu)
                if x <= tailleMax:
                    if self.tableauRed[x] != "mort":
                        self.tableauRed[x].setMouvement()
                        self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
                        #self.plateauDeJeuTK.positionJoueurRouge(self.tableauRed)
                           

        
    #Fonction  gére la gestion globale de notre application 
    def gestionDePartie (self):
        
        tempsDeplacement = 0
        self.view(self.plateauDeJeu)
        fin = 1
        
        
        while  fin ==  1:
            
            tempsDeplacement += 1
            self.plateauDeJeuTK.setTabCharacter(self.plateauDeJeu.getTableauGeneral())
            self.mouvement()
            self.view(self.plateauDeJeu) #appéle de notre fonction d'affichage

            variableFinPartie = self.conditionFinDePartie()

            if variableFinPartie == 1 :
                print("fin dE PARTIE")
                print(tempsDeplacement)
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

    


