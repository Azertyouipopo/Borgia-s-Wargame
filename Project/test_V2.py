from tkinter import*
Fenetre=Tk()
Fenetre.title("Test")
nb_Col = int(input("Col ?"))
nb_Ligne = int(input("Ligne ?"))
esp = int(input("Espace ?"))
color=input("Couleur ?")


w=0
h=0

def taille_Affichage(nb_Col,esp,nb_Ligne):
    global w
    global h
    if nb_Col >30 or nb_Ligne >30 or esp>40:
        print("ERREUR")
    if nb_Col == 20 and nb_Ligne == 20 and esp == 20:
        w=440
        h=440
    if nb_Col == 20 and nb_Ligne == 20 and esp == 10:
        h=440
        w=240
    if nb_Col == 30 and nb_Ligne == 30 and esp == 10:
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
    if nb_Col == 20 and nb_Ligne == 20 and esp == 10:
        h=440
        w=240
    if nb_Col == 10 and nb_Ligne == 20 and esp == 10:
        w=340
        h=640

## W , H  (nb_Col,esp,nb_Ligne)
##940,340 (30,30,10)
##940,650 (30,30,20)
##440,240 (20,20,10)
##440,440 (20,20,20)
##240,440 (20,10,20)
##340,640 (30,10,20)
##640,440 (20,30,20)
##840,440 (20,40,20)
##840,640 (20,40,30)
##840,240 (20,40,10)




def crea_Grille(nb_Col,esp,nb_Ligne):
    b=0
    i=0
    y=0
    test=nb_Col+1
    for b in range(nb_Ligne+1):
        m=0
        z=0
        a=0
        while z < test:
            c = zone_canvas.create_rectangle(i,0,0,y)
            i = i + esp
            z=z+1
        i=0
        y=y + nb_Col
        b=b+1

taille_Affichage(nb_Col,esp,nb_Ligne)
zone_canvas= Canvas(Fenetre, width=w,height=h,bg=color,relief="ridge")
zone_canvas.pack()
crea_Grille(nb_Col,esp,nb_Ligne)
        

