import random
from tkinter import *

subject = ['M', 'E', 'S', 'SS', 'II']
day = ['M', 'T', 'W', 'Th', 'F', 'S']

'''def shuffle():
    random.shuffle(subject)
    return list(subject)

def generate():
    a1, a2, a3, a4, a5 = shuffle(), shuffle(), shuffle(), shuffle(), shuffle()

    subjectn = (a1, a2, a3, a4, a5)


    table = {k:v for (k,v) in zip(day, subjectn)}
    return table
'''


def table(root, table):
    for i in range(len(list(table.values()))):
        for j in range(len(list(table.values())[0])):
            s = StringVar()
            s.set(list(table.values())[i][j])
            e = Entry(root, width=12, fg='blue',
                      font=('Comic Sans MS', 16, 'bold'), text=s, state=DISABLED)

            e.grid(row=i, column=j)


table1 = {'M': ['SS', 'S', 'M', 'E', 'II', '', '', ''], 'T': ['SS', 'S', 'M', 'E', 'II', '', '', ''],
          'W': ['SS', 'S', 'M', 'E', 'II', '', '', ''],
          'Th': ['SS', 'S', 'M', 'E', 'II', '', '', ''], 'F': ['SS', 'S', 'M', 'E', 'II', '', '', '']}

table2 = {'M': ['M', 'II', 'SS', 'E', 'S'], 'T': ['M', 'II', 'SS', 'E', 'S'], 'W': ['M', 'II', 'SS', 'E', 'S'],
          'Th': ['M', 'II', 'SS', 'E', 'S'], 'F': ['M', 'II', 'SS', 'E', 'S'], 'S': ['M', 'II', 'SS', 'E', 'S']}

root = Tk()

# t = table(root, table1)


menubar = Menu(root, background='grey', foreground='black')
file = Menu(menubar, tearoff=0, background='white', foreground='grey')
submenu = Menu(file, tearoff=0, background='white', foreground='grey')
submenu.add_command(label='A', command=lambda: table(root, table1))
submenu.add_command(label='B', command=lambda: table(root, table2))
file.add_cascade(label='Class10', menu=submenu)
menubar.add_cascade(label='Classes', menu=file)
root.config(menu=menubar)
root.mainloop()
