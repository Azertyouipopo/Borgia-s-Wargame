from Package.soldier import*
from tkinter import *
from random import *
verif = 0


#Fonction pour affichage des differents type de tableau




def view(plateauDeJeu):
    
    #plateauDeJeu.formatViewArray(2) # Tableau Character
    print("")
    plateauDeJeu.formatViewArray(1) #Tableau Terrain
    print("")
    #plateauDeJeu.formatViewArray(0) #Tableau Coordonees
    print("")
    #plateauDeJeu.formatViewArrayGeneral() #TableauGeneral


#Fonction qui gére l'initialisation de notre partie
#La fonction sera appelez que une seul fois par partie




    
def initialisation():

    grilleTK = PlateauDeJeuTK()
    
    
    
    nbPixelX = 820
    nbPixelY = 220
    step = 10

    
    
    plateauDeJeu = Plateau(nbPixelX,nbPixelY,step) # Instancie notre plateauDejeu
    trya = Position(plateauDeJeu,Character) # implante des soldat dans le terain
    tableauBleu = Character.blue
    
    print(Character.blue) # affichage de l'objet et de lequipe
    
    return 1,plateauDeJeu,tableauBleu # retourne 1 et notre plateauDeJeu






    
#Fonction  gére la gestion globale de notre application 
def gestion (verif):


    # IF verifier que une seulf par partie  
    if verif == 0 :
        verif,plateauDeJeu,tableauBleu = initialisation() # apppéle notre fonction d'initialisation
        
    if plateauDeJeu == None:
        print ('Erreur')
    #Instauration d'une bloucle jusqua plus de joueur enemis
    
    
    
    view(plateauDeJeu) #appéle de notre fonction d'affichage     





gestion(verif)
