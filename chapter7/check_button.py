import tkinter as tk

base = tk.Tk()
topping = {0: '海苔', 1: '煮卵', 2: 'もやし', 3: 'チャーシュー'}
check_value = {}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(base, variable=check_value[i], text=topping[i]).pack(anchor=tk.W)

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])

tk.Button(base, text='注文', command=buy).pack()

base.mainloop()
