class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character):
        
        self.plateauDeJeu = plateauDeJeu
        personnage = Character('blue',plateauDeJeu)
        personnage2 = Character('blue',plateauDeJeu)


        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[2][2] = personnage
        self.plateauDeJeu.tableauGeneral[22][2] = personnage2

        personnage.position(self.plateauDeJeu.tableauGeneral[2][0])
        personnage2.position(self.plateauDeJeu.tableauGeneral[22][0])
        
       

     
        
        
        
    
