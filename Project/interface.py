from tkinter import*
Fenetre=Tk()
Fenetre.title("Interface")
Interface= Canvas(Fenetre,width=1000,height=700,bg='red',relief="ridge")
Interface.create_rectangle(10,10,300,690)
Label(Interface, text="TEST")
Interface.pack()
