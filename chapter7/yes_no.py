import tkinter as tk
import tkinter.messagebox as msg

response = msg.askyesno('大変！！！', '大丈夫ですか？')

if response == True:
    print('大丈夫')
else:
    print('大丈夫ではない')
