from tkinter import*
##img=PhotoImage(file="Hyptosis_Sprite_Sand.png")
Fenetre=Tk()
Fenetre.title("Test")
w = int(input("Qu'elle largeur ?"))
h = int(input("Qu'elle hauteur ?"))
zone_canvas= Canvas(Fenetre, width=w,height=h,bg='red',relief="ridge")

##zone_canvas.create_rectangle(0,40,40,80)

def crea_Ligne(i,y,v,t):
    b=0
    r=i
    for b in range(10):
        m=0
        z=0
        a=0
        while z < t:
            c = zone_canvas.create_rectangle(i,0,0,y)
            i = i + t
            z=z+1
        i = 0 + r
        m=m+r
        y= y + v
        b=b+1
        print(i,z,b,m)
        while a< t:
            p = zone_canvas.create_rectangle(0,i,m,y)
            i = i + t
            a=z+1
        ##print(y)
        
        

zone_canvas.pack()
crea_Ligne(0,60,60,40)
        

