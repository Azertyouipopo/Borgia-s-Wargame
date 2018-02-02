from Package.soldier import*
from tkinter import *
from random import *
verif = 0





#Fonction pour affichage des differents type de tableau




def view(plateauDeJeu):
    
    plateauDeJeu.formatViewArray(2) # Tableau Character
    print("")
    #plateauDeJeu.formatViewArray(1) #Tableau Terrain
    print("")
    plateauDeJeu.formatViewArray(0) #Tableau Coordonees
    print("")
    #plateauDeJeu.formatViewArrayGeneral() #TableauGeneral


#Fonction qui gére l'initialisation de notre partie
#La fonction sera appelez que une seul fois par partie




    
def initialisation():

    #grilleTK = PlateauDeJeuTK()
    #nbPixelX = grilleTK.getTotalCaseTK()
    #nbPixelY = grilleTK.getTotalCaseTK()
    nbPixelX = 50
    nbPixelY = 50
    step = 10

    
    
    plateauDeJeu = Plateau(nbPixelX,nbPixelY,step) # Instancie notre plateauDejeu
    trya = Position(plateauDeJeu,Character,nbPixelX) # implante des soldat dans le terain
    tableauBleu = Character.blue
    tableauRed = Character.red
    
    #print(Character.blue) # affichage de l'objet et de lequipe
    
    return 1,plateauDeJeu,tableauBleu,tableauRed # retourne 1 et notre plateauDeJeu



def mouvementBlueTeam(indiceB,tableauBleu):
    tableauBleu[indiceB].setMouvement()
    indiceB +=1

    if indiceB == len(tableauBleu):
        return -1
    
    return indiceB

def mouvementRedTeam(indiceR,tableauBleu):
    tableauBleu[indiceR].setMouvement()
    indiceR +=1

    if indiceR == len(tableauBleu):
        return -1
    
    return indiceR

    
#Fonction  gére la gestion globale de notre application 
def gestion (verif):
    
    indiceB = 0
    indiceR = 0
    # IF verifier que une seulf par partie  
    if verif == 0 :
        verif,plateauDeJeu,tableauBleu,tableauRed = initialisation() # apppéle notre fonction d'initialisation
        
    if plateauDeJeu == None:
        print ('Erreur')
    #Instauration d'une bloucle jusqua plus de joueur enemis
    
    tempsDeplacement = 40
    view(plateauDeJeu)
    
    for i in range (0, tempsDeplacement):
        
        if indiceB != 1:
            
            indiceB = mouvementBlueTeam(indiceB,tableauBleu)
            

        if indiceR != 1:
            
           indiceR = mouvementRedTeam(indiceR,tableauRed)
        view(plateauDeJeu) #appéle de notre fonction d'affichage

           
            

def test():
    print("sqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")



gestion(verif)
