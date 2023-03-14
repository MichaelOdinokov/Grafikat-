from tkinter import *
from math import sqrt

def solver(a,b,c):

    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)
    else:
        text = "The discriminant is: %s \n This equation has no solutions" % D
    return text

def inserter(value):
    output.delete("0.0","end")
    output.insert("0.0",value)


root = Tk()
root.title("Квадратное уравнения")
tekst="Aken"
aken=Tk()
aken.geometry("500x700")# razreshenija okna
aken.title()#zagalovak

pealkiri=Label(aken, 
               text="Решение квадратного уравнения",
               bg="light blue", 
               fg="#fa9302",
               font="Algerian 20",
               height=3,
               width=23)


root.minsize(325,230)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()
a =Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="x**2+").grid(row=1,column=2)
b = Entry(frame, width=3)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)
c = Entry(frame, width=3)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)
but = Button(frame, text="Otsustama").grid(row=1, column=7, padx=(10,0))
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()