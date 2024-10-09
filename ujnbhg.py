from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Python Guides")
ws.geometry("300x250")


def about():
    messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')


menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='red', activeforeground='blue')
file = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=edit)

help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help)

ws.config(menu=menubar)
ws.mainloop()
