from tkinter import*
class PlateauDeJeuTK:

    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("test")
        self.nbCol = 0
        self.nbLigne = 0
        self.tabCord = []
        self.tabCordVOLO = []
        self.tableauPositionCoordRouge=[]
        self.setColor()
        self.setPlateau()
        self.setTailleScreen()
        self.setZoneCanvas()
        self.setCreateGrille()
        self.setPositionGrille()
        self.settest()

        
    ####### Geter #######

    def getTotalCaseTK(self):
        return self.totalCaseTK

        
    ####### Seter #######

    def setColor(self):
       self.color=input("Couleur du plateau ? (Bleu,Rouge,Vert,Jaune,Rose,Violet à écrire en anglais)")

    def setPlateau(self):
        
        print("Il ya 5 plateaux\n"
          "Plateau 1: 100 Case\n"
          "Plateau 2: 400Case\n"
          "Plateau 3: 225 Case\n"
          "Plateau 4: 625 Case\n"
          "Plateau 5: 900 Case")
        self.user = int(input("Choisisez un plateau de jeu ?"))

        if self.user == 1:
            self.nbCol=10
            self.nbLigne=10
            self.totalCaseTK = 100
        if self.user == 2:
            self.nbCol=20
            self.nbLigne=20
            self.totalCaseTK = 200
        if self.user == 3:
            self.nbCol=15
            self.nbLigne=15
            self.totalCaseTK = 150
        if self.user == 4:
            self.nbCol=25
            self.nbLigne=25
            self.totalCaseTK = 250
        if self.user == 5:
            self.nbCol=30
            self.nbLigne=30
            self.totalCaseTK = 300
        
        
    def setTailleScreen(self):
        
        if self.nbCol == 10 and self.nbLigne == 10:
            self.w=240
            self.h=240
        if self.nbCol == 20 and self.nbLigne == 20:
            self.w=440
            self.h=440
        if self.nbCol == 15 and self.nbLigne == 15:
            self.w=280
            self.h=280
        if self.nbCol == 25 and self.nbLigne == 25:
            self.w=460
            self.h=460
        if self.nbCol == 30 and self.nbLigne == 30:
            self.w=660
            self.h=660

    def setZoneCanvas(self):
        self.zoneCanvas = Canvas(self.fenetre, width = self.w, height = self.h ,bg = self.color, relief="ridge")
        

    def setCreateGrille(self):
            ## i et y sont défini a 20 pour positionné la grille sur le centre de l'affichage
        i=20
        y=40
        repeat=self.nbLigne
        tab=[]
        test = 20
        bat=40
        for b in range(repeat):
            z=0
            while z < repeat:
                c = self.zoneCanvas.create_rectangle(i,test,bat,y)
                Coord=(i,test,bat,y)
                self.tabCord.append(Coord)
                i = i + 20
                z=z+1
                bat = bat + 20
            ## Re-initialisation de i pour que la position revienne a son point initial
            i=20
            ##ajout de nb_Col a y pour décalage verticale
            test=test+20
            bat=40
            y=y+20
            b=b+1
        return(self.tabCord)
            
    def settest(self):
        self.zoneCanvas.pack()

    def setPositionGrille(self):
        x=10
        tabCordV=[]
        tabCordT=[]
        a=0
        for b in range(self.nbLigne):
            i=0
            y=10
            while i < self.nbCol:
               tabCordV= [(x,y)]
               tabCordT.append(tabCordV)
               y=y+10
               i = i+1
               self.tabCordVOLO.append(tabCordT[a])
               a=a+1
            x=x+10
        ##print(a)
        ##print(self.tabCord)
        ##print(self.tabCordVOLO)
        return (self.tabCord,self.tabCordVOLO)
                
    def setTabCharacterRouge(self,array,tableauRed):
        self.tableauCharacter=array
        self.tableauPositionCoordRouge=tableauRed
        i=0
        verif=0
        cpt=0
        nombreMortRouge = 0
        a=0
        for x in range(0,len(tableauRed)):
            if tableauRed[x] == "mort":
                nombreMortRouge += 1
        while len(tableauRed) >= nombreMortRouge:
                if self.tableauCharacter[a][2] == tableauRed [i] and verif==0:
                    self.tableauPositionCoordRouge[i]=self.tableauCharacter[a][0]
                    print(self.tableauPositionCoordRouge)
                    verif=1
                    cpt = cpt + 1
                    print('Bug 1')
                else:
                    a=a+1
                if verif == 1 and cpt <= len(tableauRed) and i < len(tableauRed):
                    i=i+1
                    verif=0
                    cpt=cpt+1
                    a=0
                    print('Bug 2')
                if verif == 1 and cpt > len(tableauRed) :
                    i=0
                    cpt=0
                    verif=0
                    a=0
                    print('Bug 3')
