from tkinter import*

class PlateauDeJeuTK:

    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("test")
        self.nbCol = 0
        self.nbLigne = 0
        self.esp = 0
        self.setColor()
        self.setPlateau()
        self.setTailleScreen()
        self.setZoneCanvas()
        self.setCreateGrille()
        self.settest()
        

        
    ####### Seter #######

    def setColor(self):
       self.color=input("Couleur du plateau ? (Bleu,Rouge,Vert,Jaune,Rose,Violet à écrire en anglais)")

    def setPlateau(self):
        
        print("Il ya 10 plateaux\n"
          "Plateau 1: 300 Case\n"
          "Plateau 2: 600 Case\n"
          "Plateau 3: 200 Case\n"
          "Plateau 4: 400 Case\n"
          "Plateau 5: 400 Case\n"
          "Plateau 6: 600 Case\n"
          "Plateau 7: 400 Case\n"
          "Plateau 8: 400 Case\n"
          "Plateau 9: 600 Case\n"
          "Plateau 10: 200 Case\n")
        self.user = int(input("Choisisez un plateau de jeu ?"))

        if self.user == 1:
            self.nbCol=30
            self.esp=30
            self.nbLigne=10
        if self.user == 2:
            self.nbCol=30
            self.esp=30
            self.nbLigne=20
        if self.user == 3:
            self.nbCol=20
            self.esp=20
            self.nbLigne=10
        if self.user == 4:
            self.nbCol=20
            self.esp=20
            self.nbLigne=20
        if self.user == 5:
            self.nbCol=20
            self.esp=10
            self.nbLigne=20
        if self.user == 6:
            self.nbCol=30
            self.esp=10
            self.nbLigne=20
        if self.user == 7:
            self.nbCol=20
            self.esp=30
            self.nbLigne=20
        if self.user == 8:
            self.nbCol=20
            self.esp=40
            self.nbLigne=20
        if self.user == 9:
            self.nbCol=20
            self.esp=40
            self.nbLigne=30
        if self.user == 10:
            self.nbCol=20
            self.esp=40
            self.nbLigne=10
        
        
    def setTailleScreen(self):
        
        if self.nbCol == 20 and self.nbLigne == 20 and self.esp == 20:
            self.w=440
            self.h=440
        if self.nbCol == 20 and self.nbLigne == 20 and self.esp == 10:
            self.h=440
            self.w=240
        if self.nbCol == 30 and self.nbLigne == 10 and self.esp == 30:
            self.w=940
            self.h=340
        if self.nbCol == 30 and self.nbLigne == 20 and self.esp == 30:
            self.w=940
            self.h=650
        if self.nbCol == 20 and self.nbLigne == 10 and self.esp == 40:
            self.w=840
            self.h=240
        if self.nbCol == 20 and self.nbLigne == 30 and self.esp == 40:
            self.w=840
            self.h=640
        if self.nbCol == 20 and self.nbLigne == 20 and self.esp == 40:
            self.w=840
            self.h=440
        if self.nbCol == 20 and self.nbLigne == 20 and self.esp == 30:
            self.w=640
            self.h=440
        if self.nbCol == 20 and self.nbLigne == 10 and self.esp == 20:
            self.w=440
            self.h=240
        if self.nbCol == 30 and self.nbLigne == 20 and self.esp == 10:
            self.w=340
            self.h=640

    def setZoneCanvas(self):
        self.zoneCanvas = Canvas(self.fenetre, width = self.w, height = self.h ,bg = self.color, relief="ridge")
        

    def setCreateGrille(self):
            ## i et y sont défini a 20 pour positionné la grille sur le centre de l'affichage
        b=0
        i=20
        y=20
        repeat= self.nbCol+1
        for b in range(self.nbLigne+1):
            z=0
            
            while z < repeat:
                c = self.zoneCanvas.create_rectangle(i,20,20,y)
                i = i + self.esp
                z=z+1
            ## Re-initialisation de i pour que la position revienne a son point initial
            i=20
            ##ajout de nb_Col a y pour décalage verticale
            y=y + self.nbCol
            b=b+1
            
    def settest(self):
        self.zoneCanvas.pack()

    ####### Geter #######

        



##select_Plateau()
##taille_Affichage(nb_Col,esp,nb_Ligne)
##zone_canvas= Canvas(Fenetre, width=w,height=h,bg=color,relief="ridge")
##crea_Grille(nb_Col,esp,nb_Ligne)
##zone_canvas.pack()
