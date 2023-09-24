from tkinter import *
 
def FartoCel():
    f=float(e1.get())
    c=(f-32)*5/9
    e2.delete(0,END)
    e2.insert(END,str(c))
def CeltoFar():
    c=int(e2.get())
    f=c*9/5.0+32
    e1.delete(0,END)
    e1.insert(END,str(f))
master = Tk()
Label(master, text="Fahrenheit").grid(row=0,column=0)
Label(master, text="Celsius").grid(row=0,column=1)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=1, column=0)
e2.grid(row=1, column=1)
e1.insert(END,"32.0")
e2.insert(END,"0.0")
 
b1 = Button(master, text=">>>", command=FartoCel)
b1.grid(row=3, column=0,padx=5, pady=5)
b2 = Button(master, text="<<<", command=CeltoFar)
b2.grid(row=3, column=1, padx=5, pady=5)
mainloop()
