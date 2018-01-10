
##################### Creation de tableau general #####################


# Crée un tableau general contenant toutes les information du plateau
def createArrayGeneral(x,y,step):
    
    # x argument represant le nombre de case collones
    # y argument represant le nombre de case ligne
    # step argument represent le pas


    # Verification si x et y  = 0 par // 10
    if x%10 != 0 or y%10 != 0:
        return False

    # Declaration de notre aire de jeu 
    tab =[]

    # Total de case present dans notre jeu
    totalCase = (x//step) * (y // step)

        

    # Boucle pour trouver coordoner
    # et construire table de jeu general 
    for o in range (0,y+1,step):
        
        for z in range (0,x+1,step):

            if z != 0 and o != 0:
             tab.append([z,o,"terre","vide"])
    
    return tab

########################################################################




    
############ Creation de tableau specifique ############


def createArrayMap(tableauGeneral):
    tab = []
    for x in range (0,len(tableauGeneral)):
        tab.append(tableauGeneral[x][2])    

    return tab




def createArrayCharacter(tableauGeneral):
    tab = []
    for x in range (0,len(tableauGeneral)):
        tab.append(tableauGeneral[x][3])
        
    return tab
        

########################################################







######## Formatage pour mode console de tableau ########



def formatViewArray(tableau,x,y):

    i = 0
    
    for o in range (0,y , 10 ):

        for z in range(0,x,10):
            
            print (tableau[i],end =" ")
            i+=1
        print ('')

        
        
########################################################

    
    
        
    

