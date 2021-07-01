from tkinter import *
from random import randint
import time

app = Tk()
app.title = 'Sorteando números'
app.geometry("700x700+350+15")
app.configure(bg = '#1E054D')

def go():
    background = Canvas(app, bg='white', heigh=500, width=500).place(x=100, y=20)
    num = randint(1, 6)
    time.sleep(0.5)
    if num == 1:
        circle = Canvas(app, bg= 'black', heigh = 70, width = 70).place(x=310, y=230)
    if num == 2:
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=430)
    if num == 3:
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=310, y=230)
    if num == 4:
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=430)
    if num == 5:
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=310, y=230)
    if num == 6:
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=40)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=430)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=120, y=230)
        circle = Canvas(app, bg='black', heigh=70, width=70).place(x=500, y=230)

background = Canvas(app, bg = 'white', heigh = 500, width = 500).place(x=100, y=20)

Sortear = Button(app, bg = '#450B45', text= 'Sort', width = 12, heigh = 3, fg = 'white', font=90, command= go).place(x=285, y = 580)

app.mainloop()