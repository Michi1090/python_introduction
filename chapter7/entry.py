from random import triangular
import tkinter as tk

base = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(base, textvariable=string).pack()
label = tk.Label(base, textvariable=string).pack()

base.mainloop()
