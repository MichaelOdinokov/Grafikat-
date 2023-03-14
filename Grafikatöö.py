from tkinter import*
from Omamodul import*


tekst="Aken"
aken=Tk()
aken.geometry("900x720")# razreshenija okna
aken.title()#zagalovak


pealkiri=Label(aken, 
               text="Решение квадратного уравнения",
               bg="light blue", 
               fg="green",
               font="Algerian 20",
               height=3,
               width=50)# label raspredljaem tekst fg palitra zvetov,  font=(nazvanija shrifta, Forte)

raam=Canvas(aken,
            width=260,
            height=260,
            bg="black")



tekst_kast=Entry(aken,
                 fg="green",
                 bg="light blue",
                 font="Algerian 20",
                 width=2,
                 justify=LEFT)
tekst_kast.bind("<Return>", text_to_lbl)






pealkiri.pack()# upakovka elementov
tekst_kast.pack()#side=LEFT, RIGHT

raam.pack()
aken.mainloop()# v samom konze
