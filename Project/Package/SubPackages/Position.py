class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    def __init__(self,plateauDeJeu,Character):

        self.plateauDeJeu = plateauDeJeu
        personnage = Character('blue')
        personnage2 = Character('blue')
        
        self.plateauDeJeu.tableauGeneral[2][2] = personnage
        personnage.setPosition = self.plateauDeJeu.tableauGeneral[2][0]
        
        self.plateauDeJeu.tableauGeneral[22][2] = personnage2
        personnage.setPosition = self.plateauDeJeu.tableauGeneral[22][0]
        
        
        
    
