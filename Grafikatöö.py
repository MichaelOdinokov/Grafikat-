from tkinter import*
from Omamodul import*

def klikker():
    global k
    k+=1
    nupp.configure(text=k)#menjaet parametri

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

tekst="Aken"
aken=Tk()
aken.geometry("1080x720")# razreshenija okna
aken.title()#zagalovak

pealkiri=Label(aken, 
               text="Решение квадратного уравнения",
               bg="light blue", 
               fg="green",
               font="Algerian 20",
               height=-3,
               width=23)# label raspredljaem tekst fg palitra zvetov,  font=(nazvanija shrifta, Forte)

raam=Canvas(aken,
            width=300,
            height=400,
            bg="black")

tekst_kast=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=20,
                 justify=CENTER)
tekst_kast.bind("<Return>")# sobitija , a potom funktsuju return=enter

tekst_kast=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=2,
                 justify=CENTER)
tekst_kast.bind("<Return>")# sobitija , a potom funktsuju return=enter

nupp=Button(aken,
            text="Vajuta mind",            
            fg="#836aa1",
            font="Algerian 20",
            activebackground="green",
            height=3,
            width=20,
            command=klikker)# delaem knopku. Command standartnaja funktsija

pealkiri.pack()# upakovka elementov
tekst_kast.pack()#side=LEFT, RIGHT
raam.pack()
aken.mainloop()# v samom konze
