from tkinter import*
from Omamodul import*

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

def klikker():
    global k
    k+=1
    nupp.configure(text=k)
    


tekst="Aken"
aken=Tk()

aken.geometry("600x720")
aken.title()


pealkiri=Label(aken, 
               text="Ruutvõrrandi lahendamine",
               bg="light blue", 
               fg="green",
               font="Algerian 20",
               height=3,
               width=23)
tekst_kast=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=2,
                 justify=CENTER)
tekst_kast.bind("<Return>", text_to_lbl)

tekst_kas=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=2,
                 justify=CENTER)
tekst_kas.bind("<Return>", text_to_lbl)

tekst_ka=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=2,
                 justify=CENTER)
tekst_ka.bind("<Return>", text_to_lbl)

nupp=Button(aken,
            text="Lahendada",
            bg="green",
            fg="black",
            font="Algerian 20",
            height=5,
            width=10,
            command=klikker)



pealkiri.pack()
tekst_kast.pack()
tekst_kas.pack() 
tekst_ka.pack()
nupp.pack()



aken.mainloop()
