from random import *
class Position:
    #Classe qui permet l'insertion de personnage dans le tableaus

    tableauClasseAlgo =[]
    
    def __init__(self,plateauDeJeu,Character,Fantassin,Bretteur,Chevalier,nbPixelX,index):
        
        self.plateauDeJeu = plateauDeJeu
        self.nbPixelX = nbPixelX
        self.Index = index
        self.Character = Character
        self.Fantassin = Fantassin
        self.Bretteur = Bretteur
        self.Chevalier = Chevalier
        self.tableauDeClasse = [self.Fantassin,self.Bretteur,self.Chevalier]
        self.nombreDeClasse = len(self.tableauDeClasse)
        self.algoClasse(self)
        varControl = 0
        
        while varControl == 0 :
            i = int(input("Combien d'argent possédée vous ?"))
            if i >  0 :
                break

        
        
        
        self.test = self.algoChoixDeClasse()
        self.test1 = self.algoChoixDeClasse()
        self.test2 = self.algoChoixDeClasse()
        self.personnage = self.test('blue',plateauDeJeu,nbPixelX,"personnage",index)
        self.personnage4 = self.test1('blue',plateauDeJeu,nbPixelX,"personnage4",index)
        self.personnage5 = self.test2('blue',plateauDeJeu,nbPixelX,"personnage5",index)

        # qui insére ces coordonée de postion d'apres le tableauGeneral
        self.plateauDeJeu.tableauGeneral[90][2] = self.personnage
        self.plateauDeJeu.tableauGeneral[91][2] = self.personnage4
        self.plateauDeJeu.tableauGeneral[92][2] = self.personnage5
        
        

        self.personnage.setPosition(self.plateauDeJeu.tableauGeneral[90][0])
        self.personnage4.setPosition(self.plateauDeJeu.tableauGeneral[91][0])
        self.personnage5.setPosition(self.plateauDeJeu.tableauGeneral[92][0]) 

        self.initArmeeRouge()

        
    
         
    @staticmethod
    def algoClasse(self):
        if len(self.tableauClasseAlgo) == 0 :
            pourcentageSpawn = 100 / self.nombreDeClasse
            for i in range (0 , len(self.tableauDeClasse)):
                self.tableauClasseAlgo.append([self.tableauDeClasse[i],pourcentageSpawn])
            return 0
        
    def algoChoixDeClasse(self):
        i = 0
        while i != 1 :
            choixClassRand = randrange(0, self.nombreDeClasse, 1)
            choixClassRandPerso = randrange(0, 100 , 1) 
            if self.tableauClasseAlgo[choixClassRand][1] >= choixClassRandPerso:
                return(self.tableauClasseAlgo[choixClassRand][0])
                 
                
        
        
       
    def initArmeeRouge(self):

        stop = 0
        tableau = []
        while stop == 0:
            
            soldatPersonnage =int(input("Combien de Fantassin est composée de l'equipe énemies !"))

            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Fantassin("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)
                    
            soldatPersonnage =int(input("Combien de Bretteur est composée de l'equipe énemies !"))
            
            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Bretteur("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)

            soldatPersonnage =int(input("Combien de Chevalier est composée de l'equipe énemies !"))
            
            if soldatPersonnage > 0 and soldatPersonnage < self.nbPixelX  :
                for i in range(0,soldatPersonnage):
                    self.i = self.Chevalier("red",self.plateauDeJeu,self.nbPixelX,str(i),self.Index)
                    tableau.append(self.i)
                    shuffle(tableau)
                print(tableau)
            
            for x in range(0,len(tableau)):
                    self.plateauDeJeu.tableauGeneral[x][2] = tableau[x]
                    
            for y in range(0,len(tableau)):
                tableau[y].setPosition(self.plateauDeJeu.tableauGeneral[y][0])
                    
            break
              
        
        
        
    
