class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character,nbPixelX,index):
        
        self.plateauDeJeu = plateauDeJeu
        personnage = Character('blue',plateauDeJeu,nbPixelX,"personnage",index)
        personnage4 = Character('blue',plateauDeJeu,nbPixelX,"personnage4",index)
        personnage2 = Character('red',plateauDeJeu,nbPixelX,"personnage2",index)
        personnage3 = Character('red',plateauDeJeu,nbPixelX,"personnage3",index)

        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[2][2] = personnage
        self.plateauDeJeu.tableauGeneral[7][2] = personnage4
        self.plateauDeJeu.tableauGeneral[20][2] = personnage2
        self.plateauDeJeu.tableauGeneral[24][2] = personnage3
        

        personnage.setPosition(self.plateauDeJeu.tableauGeneral[2][0])
        personnage4.setPosition(self.plateauDeJeu.tableauGeneral[7][0]) 
        personnage2.setPosition(self.plateauDeJeu.tableauGeneral[20][0])
        personnage3.setPosition(self.plateauDeJeu.tableauGeneral[24][0])
        
       

     
        
        
        
    
