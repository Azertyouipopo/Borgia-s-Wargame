class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character,nbPixelX,index):
        
        self.plateauDeJeu = plateauDeJeu
        self.nbPixelX = nbPixelX
        self.Index = index
        self.Character = Character
        
        self.personnage = Character('blue',plateauDeJeu,nbPixelX,"personnage",index)
        self.personnage4 = Character('blue',plateauDeJeu,nbPixelX,"personnage4",index)
        

        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[800][2] = self.personnage
        self.plateauDeJeu.tableauGeneral[850][2] = self.personnage4
        
        

        self.personnage.setPosition(self.plateauDeJeu.tableauGeneral[800][0])
        self.personnage4.setPosition(self.plateauDeJeu.tableauGeneral[850][0]) 
        

        self.initArmeeRouge()
    
         
        
       
    def initArmeeRouge(self):

        stop = 0
        tableau = []
        while stop == 0:
            soldatPersonnage =int(input("Combien de Personnage est composée de l'equipe énemies !"))
            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Character("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)
                    
                for x in range(0,len(tableau)):
                    self.plateauDeJeu.tableauGeneral[x][2] = tableau[x]
                    
                for y in range(0,len(tableau)):
                    tableau[y].setPosition(self.plateauDeJeu.tableauGeneral[y][0])
                    
            break
              
        
        
        
    
