class Insertion:

    compteur = 0;
    
    
    def __init__(self,plateauDeJeu):
        self.plateauDeJeu = plateauDeJeu
        
        
    def positionCharachter (self):

        tab = self.plateauDeJeu.tableauGeneral
        personnage = Character()
        tab[2][2] = Character()       
