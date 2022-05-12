import tkinter as tk

base = tk.Tk()
button1 = tk.Button(base, text='PUSH1', width=20).pack()
button2 = tk.Button(base, text='PUSH2').pack(side=tk.LEFT)
button3 = tk.Button(base, text='PUSH3').pack(side=tk.RIGHT)

base.mainloop()
