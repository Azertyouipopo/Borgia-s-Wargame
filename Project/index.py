from Package.soldier import*
from tkinter import *
from random import *
verif = 0



def view(plateauDeJeu):
    
    plateauDeJeu.formatViewArray(2)
    print("")
    plateauDeJeu.formatViewArray(1)
    print("")
    plateauDeJeu.formatViewArray(0)
    print("")
    plateauDeJeu.formatViewArrayGeneral()
    
def initialisation():
    nbPixelX = 50
    nbPixelY = 50
    step = 10
    plateauDeJeu = Plateau(nbPixelX,nbPixelY,step)
    trya = Position(plateauDeJeu,Character)

    print(Character.blue)
    
    return 1,plateauDeJeu
    

def gestion (verif):

    if verif == 0 :
        verif,plateauDeJeu = initialisation()
        
    if plateauDeJeu == None:
        print ('Erreur')
    #Instauration d'une bloucle jusqua plus de joueur enemis
    
    
    view(plateauDeJeu)    


gestion(verif)
