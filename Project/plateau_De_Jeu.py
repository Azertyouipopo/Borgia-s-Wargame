from tkinter import*
Fenetre=Tk()
Fenetre.title("Test")

nb_Col=0
nb_Ligne=0
esp=0


color=input("Couleur du plateau ? (Bleu,Rouge,Vert,Jaune,Rose,Violet à écrire en anglais)")

##Fonction qui demande à l'utilisateur de choisir le plateau de jeu
def select_Plateau():
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
    user = int(input("Choisisez un plateau de jeu ?"))
    global nb_Col
    global esp
    global nb_Ligne
    if user == 0 or user > 10:
        print("Veuillez séléctioner un plateau de jeu !")
        user = int(input("Choisisez un plateau de jeu parmi les 10 proposé seulement !"))
    if user == 1:
        nb_Col=30
        esp=30
        nb_Ligne=10
    if user == 2:
        nb_Col=30
        esp=30
        nb_Ligne=20
    if user == 3:
        nb_Col=20
        esp=20
        nb_Ligne=10
    if user == 4:
        nb_Col=20
        esp=20
        nb_Ligne=20
    if user == 5:
        nb_Col=20
        esp=10
        nb_Ligne=20
    if user == 6:
        nb_Col=30
        esp=10
        nb_Ligne=20
    if user == 7:
        nb_Col=20
        esp=30
        nb_Ligne=20
    if user == 8:
        nb_Col=20
        esp=40
        nb_Ligne=20
    if user == 9:
        nb_Col=20
        esp=40
        nb_Ligne=30
    if user == 10:
        nb_Col=20
        esp=40
        nb_Ligne=10
    


w=0
h=0
##Fonction d'affichage/réglage de l'interface
def taille_Affichage(nb_Col,esp,nb_Ligne):
    global w
    global h
    if nb_Col == 20 and nb_Ligne == 20 and esp == 20:
        w=440
        h=440
    if nb_Col == 20 and nb_Ligne == 20 and esp == 10:
        h=440
        w=240
    if nb_Col == 30 and nb_Ligne == 10 and esp == 30:
        w=940
        h=340
    if nb_Col == 30 and nb_Ligne == 20 and esp == 30:
        w=940
        h=650
    if nb_Col == 20 and nb_Ligne == 10 and esp == 40:
        w=840
        h=240
    if nb_Col == 20 and nb_Ligne == 30 and esp == 40:
        w=840
        h=640
    if nb_Col == 20 and nb_Ligne == 20 and esp == 40:
        w=840
        h=440
    if nb_Col == 20 and nb_Ligne == 20 and esp == 30:
        w=640
        h=440
    if nb_Col == 20 and nb_Ligne == 10 and esp == 20:
        w=440
        h=240
    if nb_Col == 30 and nb_Ligne == 20 and esp == 10:
        w=340
        h=640



def crea_Grille(nb_Col,esp,nb_Ligne):
    ## i et y sont défini a 20 pour positionné la grille sur le centre de l'affichage
    b=0
    i=20
    y=20
    repeat=nb_Col+1
    for b in range(nb_Ligne+1):
        m=0
        z=0
        a=0
        while z < repeat:
            c = zone_canvas.create_rectangle(i,20,20,y)
            i = i + esp
            z=z+1
        ## Re-initialisation de i pour que la position revienne a son point initial
        i=20
        ##ajout de nb_Col a y pour décalage verticale
        y=y + nb_Col
        b=b+1

select_Plateau()
taille_Affichage(nb_Col,esp,nb_Ligne)
zone_canvas= Canvas(Fenetre, width=w,height=h,bg=color,relief="ridge")
crea_Grille(nb_Col,esp,nb_Ligne)
zone_canvas.pack()
