from tkinter import *
def clickButton(a):
    a = -a
    feLabel = Label(text="its iron")
    if a > 0:
        feLabel.pack()
    else:
        feLabel.destroy()
    return a