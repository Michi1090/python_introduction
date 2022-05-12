import tkinter as tk

base = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0: 'Aランチ', 1: 'Bランチ', 2: 'Cランチ'}

tk.Radiobutton(base, text=lunch[0], variable=radio_value, value=0).pack()
tk.Radiobutton(base, text=lunch[1], variable=radio_value, value=1).pack()
tk.Radiobutton(base, text=lunch[2], variable=radio_value, value=2).pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

tk.Button(base, text='注文', command=buy).pack()

base.mainloop()
