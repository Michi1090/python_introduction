import tkinter as tk

base = tk.Tk()

def fileopen():
    print('ファイルを開く処理')

menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='ファイル', menu=filemenu)
filemenu.add_command(label='ファイルを開く', command=fileopen)
base.config(menu=menubar)

base.mainloop()
