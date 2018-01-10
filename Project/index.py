from Package.soldier import*
from tkinter import *
from random import *

view = Character()


# fonction pour poser soldat

def putCharacter(totalCase,tab):
    w = 0
    position = randrange(0, totalCase, 1)
    personnage = Character
    tab[position][3] = personnage
    return tab
    

def view(tableauGeneral,x,y):
    formatViewArray(tableauGeneral,x,y,3)

def gestion ():
    
    nbPixelX = 50
    nbPixelY = 50
    step = 10
    
    tableauGeneral,totalCase = createArrayGeneral(nbPixelX,nbPixelY,step)
    if tableauGeneral == False:
        print ('Erreur')

    tableauGeneral = putCharacter(totalCase,tableauGeneral)
    view(tableauGeneral,nbPixelX,nbPixelY)


gestion()
