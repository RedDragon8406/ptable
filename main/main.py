import tkinter as tk
from maduels import *
a = 1 # agar a ro manfi kone chap mikone faghat man daram ro in ghesmat kar mikonam
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="fe",command=clickButton(a))
slogan.pack(side=tk.LEFT)
root.mainloop()