from Package.soldier import*
from tkinter import *

view = Character()



def gestion ():
    
    tableauGeneral = createArrayGeneral(60,60,10)
    if tableauGeneral == False:
        print ('Erreur')

    tableauMap = createArrayMap(tableauGeneral)
    tableauCharacter = createArrayCharacter(tableauGeneral)
    formatViewArray(tableauMap,60,60)

