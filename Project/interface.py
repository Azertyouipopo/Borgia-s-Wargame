from tkinter import*
Fenetre=Tk()
Fenetre.title("Interface")
Interface= Canvas(Fenetre,width=1000,height=700,bg='red',relief="ridge")
Interface.create_rectangle(10,10,300,690)
Frame1= Frame(Interface, relief="ridge",bg='blue',borderwidth=2)
Frame1.pack(side=LEFT, padx=30, pady=30)
Label(Frame1, text="TEST").pack(padx=10, pady=10)
Interface.pack()
