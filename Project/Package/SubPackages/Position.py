class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character,nbPixelX):
        
        self.plateauDeJeu = plateauDeJeu
        personnage = Character('blue',plateauDeJeu,nbPixelX)
        personnage2 = Character('blue',plateauDeJeu,nbPixelX)


        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[2][2] = personnage
        self.plateauDeJeu.tableauGeneral[20][2] = personnage
     
        

        personnage.position(self.plateauDeJeu.tableauGeneral[2][0])
        personnage2.position(self.plateauDeJeu.tableauGeneral[20][0])
        
       

     
        
        
        
    
