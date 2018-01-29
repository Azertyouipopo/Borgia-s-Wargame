from tkinter import*
Fenetre=Tk()
Fenetre.title("Test")

nb_Col=0
nb_Ligne=0
tabCord=[]


color=input("Couleur du plateau ? (Bleu,Rouge,Vert,Jaune,Rose,Violet à écrire en anglais)")

##Fonction qui demande à l'utilisateur de choisir le plateau de jeu
def select_Plateau():
    user = int(input("Choisisez un plateau de jeu ?"))
    global nb_Col
    global esp
    global nb_Ligne
    while user == 0 or user > 5:
        print("Veuillez séléctioner un plateau de jeu !")
        user = int(input("Choisisez un plateau de jeu parmi les 10 proposé seulement !"))
    if user == 1:
        nb_Col=10
        nb_Ligne=10
    if user == 2:
        nb_Col=20
        nb_Ligne=20
    if user == 3:
        nb_Col=15
        nb_Ligne=15
    if user == 4:
        nb_Col=25
        nb_Ligne=25
    if user == 5:
        nb_Col=30
        nb_Ligne=30

    


w=0
h=0
##Fonction d'affichage/réglage de l'interface
def taille_Affichage(nb_Col,nb_Ligne):
    global w
    global h
    if nb_Col == 10 and nb_Ligne == 10:
        w=440
        h=440
    if nb_Col == 20 and nb_Ligne == 20:
        w=640
        h=640
    if nb_Col == 15 and nb_Ligne == 15:
        w=480
        h=480
    if nb_Col == 25 and nb_Ligne == 25:
        w=660
        h=660
    if nb_Col == 30 and nb_Ligne == 30:
        w=730
        h=1000



def creaGrille(nb_Col,nb_Ligne,tabCord):
    ## i et y sont défini a 20 pour positionné la grille sur le centre de l'affichage
    b=0
    MultiLi=nb_Ligne
    MultiCo=nb_Col
    if nb_Col == 10:
        MultiLi=MultiLi*4
        MultiCo=MultiCo*4
    if nb_Col == 15:
        MultiLi=MultiLi*2
        MultiCo=MultiCo*2
    if nb_Col == 20:
        MultiLi=MultiLi*1.5
        MultiCo=MultiCo*1.5
    if nb_Col == 30:
        MultiLi=MultiLi*0.75
        MultiCo=MultiCo*0.75
    i=MultiLi
    y=20
    repeat=nb_Col
    tab=[]
    for b in range(nb_Ligne):
        z=0
        while z < repeat:
            c = zone_canvas.create_rectangle(y,y,(i+20),(i+20))
            tet= (y,y,i,i)
            tabCord.append(tet)
            i = i + MultiLi
            z=z+1
        ## Re-initialisation de i pour que la position revienne a son point initial
        i=MultiLi
        ##ajout de nb_Col a y pour décalage verticale
        y=y + MultiCo
        b=b+1
    print(tabCord)
    print('')
    return(tabCord)

def setPositionGrille(tabCord,nb_Col,nb_Ligne):
    y=10
    tabCordV=[]
    tabCordT=[]
    a=0
    for b in range(nb_Ligne):
        i=0
        x=10
        while i < nb_Col:
           tabCordV= [(x,y)]
           tabCordT.append(tabCordV)
           x=x+10
           i = i+1
           tabCord[a]=tabCordT[a]
           a=a+1
        y=y+10
    print(tabCord)

select_Plateau()
taille_Affichage(nb_Col,nb_Ligne)
zone_canvas= Canvas(Fenetre, width=w,height=h,bg=color,relief="ridge")
creaGrille(nb_Col,nb_Ligne,tabCord)
setPositionGrille(tabCord,nb_Col,nb_Ligne)
zone_canvas.pack()
