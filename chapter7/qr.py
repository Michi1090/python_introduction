import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk

# コンソールの配置
base = tk.Tk()
base.title('QRcode Generator')
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)

# URLとQRコードの入出力
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)
qr_label = tk.Label(image_area)

# QRコードの作成と表示
def generate():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()

# ボタンの作成
encode_button = tk.Button(input_area, text='QRcode', command=generate).pack(side=tk.LEFT)
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)

# 保存メニュー
def save():
    filename = fd.asksaveasfilename(title='名前をつけて保存する', initialfile='prcode.png')
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

# 終了メニュー
def exit():
    base.destroy()

# メニュー画面
menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='save', command=save)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
base.config(menu=menubar)

# 画面の永久表示
base.mainloop()
