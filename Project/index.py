from Package.soldier import*
from tkinter import *
from random import *
verif = 0



# fonction pour poser soldat

def putCharacter(plateauDeJeu):
    
   
    x=0
    while x < 1:
        tab = plateauDeJeu.getTableauGeneral() #Recuperation du tableau general
        totalCase = plateauDeJeu.getTotalCase()#Recuperation du nombre de case
        position = randrange(0, totalCase, 1)#Genere un nombre aleatoire entre 0 et totalcase
        personnage = Character()#Instance d'un objet personnage 
        tab[position][2] = personnage #Donne au tableauGeneral l'emplacement de l'objet
        personnage.setPosition(tab[position][0]) #Donne à notre objet sont emplacement dans le tableau
        
        x+=1    
    return personnage
    


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
    personnage =putCharacter(plateauDeJeu)
    return 1,plateauDeJeu,personnage
    

def gestion (verif):

    if verif == 0 :
        verif,plateauDeJeu,personnage = initialisation()
        
    if plateauDeJeu == None:
        print ('Erreur')
    #Instauration d'une bloucle jusqua plus de joueur enemis
    
    personnage.deplacement()
    view(plateauDeJeu)
      


gestion(verif)
