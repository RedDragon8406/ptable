from tkinter import *
import tkinter.messagebox
#======================== setting ===========================
root = tkinter.Tk()
root.title('ptable')
root.geometry('800x600')
root.resizable(False,False)
root.config(bg='gray')
#======================== variables ===========================

color = 'gray'
#hydro
xH = IntVar()
xH.set(0)
H = Label(root,text='hydrogen',bg=color,fg='yellow',font = '10')
#iron
xFe = IntVar()
xFe.set(0)
Fe = Label(root,text='iron',bg=color,fg='yellow',font='10')
#======================== Functios ===========================

def hydro(n,label):
    if n.get() == 0:
        label.pack()
        n.set(1)
    else:
        label.forget()
        n.set(0)
#======================== frames ===========================
#======================== buttons ===========================
btn_H = Button(root,text='H',width='10',height='2',bg='cyan',command=lambda : hydro(xH,H))
btn_H.place(x = 10 , y =30)
btn_Fe = Button(root,text='Fe',width='10',height='2',bg='cyan',command=lambda : hydro(xFe,Fe))
btn_Fe.place(x = 100 , y = 30)

root.mainloop()