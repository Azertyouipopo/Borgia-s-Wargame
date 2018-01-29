from tkinter import*

class PlateauDeJeuTK:

    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("test")
        self.nbCol = 0
        self.nbLigne = 0
        self.tabCord = []
        self.setColor()
        self.setPlateau()
        self.setTailleScreen()
        self.setZoneCanvas()
        self.setCreateGrille()
        self.setPositionGrille()
        self.settest()
        

        
    ####### Seter #######

    def setColor(self):
       self.color=input("Couleur du plateau ? (Bleu,Rouge,Vert,Jaune,Rose,Violet à écrire en anglais)")

    def setPlateau(self):
        
        print("Il ya 10 plateaux\n"
          "Plateau 1: 100 Case\n"
          "Plateau 2: 400Case\n"
          "Plateau 3: 225 Case\n"
          "Plateau 4: 625 Case\n"
          "Plateau 5: 900 Case")
        self.user = int(input("Choisisez un plateau de jeu ?"))

        if self.user == 1:
            self.nbCol=10
            self.nbLigne=10
        if self.user == 2:
            self.nbCol=20
            self.nbLigne=20
        if self.user == 3:
            self.nbCol=15
            self.nbLigne=15
        if self.user == 4:
            self.nbCol=25
            self.nbLigne=25
        if self.user == 5:
            self.nbCol=30
            self.nbLigne=30
        
        
    def setTailleScreen(self):
        
        if self.nbCol == 10 and self.nbLigne == 10:
            self.w=440
            self.h=440
        if self.nbCol == 20 and self.nbLigne == 20:
            self.w=640
            self.h=640
        if self.nbCol == 15 and self.nbLigne == 15:
            self.w=480
            self.h=480
        if self.nbCol == 25 and self.nbLigne == 25:
            self.w=660
            self.h=660
        if self.nbCol == 30 and self.nbLigne == 30:
            self.w=730
            self.h=1000

    def setZoneCanvas(self):
        self.zoneCanvas = Canvas(self.fenetre, width = self.w, height = self.h ,bg = self.color, relief="ridge")
        

    def setCreateGrille(self):
            ## i et y sont défini a 20 pour positionné la grille sur le centre de l'affichage
        MultiLi=self.nbLigne
        MultiCo=self.nbCol
        if self.nbCol == 10:
            MultiLi=MultiLi*4
            MultiCo=MultiCo*4
        if self.nbCol == 15:
            MultiLi=MultiLi*2
            MultiCo=MultiCo*2
        if self.nbCol == 20:
            MultiLi=MultiLi*1.5
            MultiCo=MultiCo*1.5
        if self.nbCol == 30:
            MultiLi=MultiLi*0.75
            MultiCo=MultiCo*0.75
        i=MultiLi
        y=20
        repeat=self.nbCol
        tab=[]
        for b in range(self.nbLigne):
            z=0
            while z < repeat:
                c = self.zoneCanvas.create_rectangle(y,y,(i+20),(i+20))
                Coord=(y,y,i,i)
                self.tabCord.append(Coord)
                i = i + MultiLi
                z=z+1
            ## Re-initialisation de i pour que la position revienne a son point initial
            i=MultiLi
            ##ajout de nb_Col a y pour décalage verticale
            y=y + MultiCo
            b=b+1
        return(self.tabCord)
            
    def settest(self):
        self.zoneCanvas.pack()

    def setPositionGrille(self):
        y=10
        tabCordV=[]
        tabCordT=[]
        a=0
        for b in range(self.nbLigne):
            i=0
            x=10
            while i < self.nbCol:
               tabCordV= [(x,y)]
               tabCordT.append(tabCordV)
               x=x+10
               i = i+1
               self.tabCord[a]=tabCordT[a]
               a=a+1
            y=y+10
        print(self.tabCord)

    ####### Geter #######

        



##select_Plateau()
##taille_Affichage(nb_Col,esp,nb_Ligne)
##zone_canvas= Canvas(Fenetre, width=w,height=h,bg=color,relief="ridge")
##crea_Grille(nb_Col,esp,nb_Ligne)
##zone_canvas.pack()
