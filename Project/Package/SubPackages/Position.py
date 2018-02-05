class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character,nbPixelX,index):
        
        self.plateauDeJeu = plateauDeJeu
        self.personnage = Character('blue',plateauDeJeu,nbPixelX,"personnage",index)
        self.personnage4 = Character('blue',plateauDeJeu,nbPixelX,"personnage4",index)
        self.personnage2 = Character('red',plateauDeJeu,nbPixelX,"personnage2",index)
        self.personnage3 = Character('red',plateauDeJeu,nbPixelX,"personnage3",index)

        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[2][2] = self.personnage
        self.plateauDeJeu.tableauGeneral[7][2] = self.personnage4
        self.plateauDeJeu.tableauGeneral[20][2] = self.personnage2
        self.plateauDeJeu.tableauGeneral[24][2] =self.personnage3
        

        self.personnage.setPosition(self.plateauDeJeu.tableauGeneral[2][0])
        self.personnage4.setPosition(self.plateauDeJeu.tableauGeneral[7][0]) 
        self.personnage2.setPosition(self.plateauDeJeu.tableauGeneral[20][0])
        self.personnage3.setPosition(self.plateauDeJeu.tableauGeneral[24][0])

    
         
        
       

     
        
        
        
    
