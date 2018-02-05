class Plateau:
    


    ##################### Creation de tableau general #####################


    # Crée un tableau general contenant toutes les information du plateau
    def __init__(self,x,y,step):
        
          
        # Verification si x et y  = 0 par // 10
        if x%10 != 0 or y%10 != 0:
            print('tolo')
            return None

        

        
        self.x = x # x argument represant le nombre de case collones
        self.y = y  # y argument represant le nombre de case ligne
        self.step = step # step argument represent le pas 
        self.tableauGeneral =[] # Declaration de notre aire de jeu 
        self.totalCase = (self.x//self.step) * (self.y // self.step) # Total de case present dans notre jeu
        print(self.totalCase)
            
        # Boucle pour trouver coordoner
        # et construire table de jeu general 
        for o in range (0,self.y+1,self.step):
            
            for z in range (0,self.x+1,self.step):

                if z != 0 and o != 0:
                    self.tableauGeneral.append([[z,o],"terre","vide"])
                    
        self.createArrayCoordone()         
        self.createArrayMap()
        self.createArrayCharacter()
        
        
    
    ################## Creation de tableau specifique  #####################

    def createArrayCoordone(self):
        tab = []
        
        for n in range (0,len(self.tableauGeneral)):
            tab.append(self.tableauGeneral[n][0])
            
            
        
        
    def createArrayMap(self):
        tab = []
        for x in range (0,len(self.tableauGeneral)):
            tab.append(self.tableauGeneral[x][1])    
        self.tableauMap = tab
        




    def createArrayCharacter(self):
        tab = []
        for x in range (0,len(self.tableauGeneral)):
            
            tab.append(self.tableauGeneral[x][2])
        self.tableauCharacter = tab
        
        

    
    

    

    ########################### Formatage  #############################


    
    def formatViewArray(self,a):

        i = 0

        
        
        for o in range (0,self.y , 10 ):

            for z in range(0,self.x,10):
                
                print (self.tableauGeneral[i][a],end =" " )
                i+=1
            print ('')
        


    def formatViewArrayGeneral(self):

        i = 0

        for o in range (0,self.y , 10 ):

            for z in range(0,self.x,10):
                
                print (self.tableauGeneral[i],end =" " )
                i+=1
            print ('')
        
        
    ########################### Geteur  #############################
    
    def getTableauGeneral(self):
        return self.tableauGeneral

    def getTableauCharacter(self):
        return self.tableauCharacter

    def getTotalCase(self):
        return self.totalCase
    
    
    ########################### Seteur  #############################

    def setTableauGeneral(self,tab):
        self.tableauGeneral = tab
        
