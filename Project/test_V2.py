from tkinter import*
Fenetre=Tk()
Fenetre.title("Test")
nb_Col = int(input("Col ?"))
nb_Ligne = int(input("Ligne ?"))
esp = int(input("Espace ?"))

def taille_Affichage(nb_Col,esp,nb_Ligne):
    h=0
    w=0
    if nb_Col >30 or nb_Ligne >30 or esp>40:
        print("ERREUR")
    if nb_Col == 20 and nb_Ligne == 20 and esp == 20:
        w=440
        h=440
    if nb_Col == 20 and nb_Ligne == 20 and esp == 10:
        w=440
        h=240
    return w,h
        



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

## i indique l'espacement entre les lignes ligne

zone_canvas= Canvas(Fenetre, width=w,height=h,bg='red',relief="ridge")
zone_canvas.pack()
taille_Affichage(nb_Col,esp,nb_Ligne)
crea_Grille(nb_Col,esp,nb_Ligne)
        

