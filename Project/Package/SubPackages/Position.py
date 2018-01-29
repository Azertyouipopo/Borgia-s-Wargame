class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character):
        
        self.plateauDeJeu = plateauDeJeu
        personnage = Character('blue',plateauDeJeu)
        personnage2 = Character('blue',plateauDeJeu)


        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[502][2] = personnage
        

        personnage.position(self.plateauDeJeu.tableauGeneral[2][0])
        
        
       

     
        
        
        
    
