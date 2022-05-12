import tkinter as tk

base = tk.Tk()
def push():
    print('MELON!')

button = tk.Button(base, text='WATER', command=push).pack()

base.mainloop()
