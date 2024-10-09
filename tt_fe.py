import tkinter as tk
import tkinter.simpledialog as dl
import mysql.connector as sq
import tt_be as be

#print('working')


def menu(window, d_base='timetables'):
    be.database(d_base)
    db.execute(f'use {d_base}')

    global menubar
    menubar = tk.Menu(root)

    # For Classes in database
    class_ = tk.Menu(menubar, tearoff=False)
    db.execute('select * from grades')

    for table in sorted(db.fetchall()):
        db.execute(f'select sec from grades where class="{table[0]}"')
        sections = db.fetchall()[0][0].split(',')

        submenu = tk.Menu(class_, tearoff=False)
        for section in filter(None, sorted(sections)):
            submenu.add_command(label=section,
                                command=lambda grd=table[0], sect=section: display(window, grd, sect))
        class_.add_cascade(label=table[0], menu=submenu)
    menubar.add_cascade(label='Classes', menu=class_)

    window.config(menu=menubar)


def add_menu(window):
    # noinspection PyUnboundLocalVariable
    global edit
    edit = tk.Menu(menubar, tearoff=False)

    def refresh():
        for widgets in window.winfo_children():
            if repr(widgets).startswith('<tkinter.Menu object .!menu'):
                widgets.destroy()

            global menubar
            menubar = tk.Menu(window)
            menu(window)
            add_menu(window)

    def add():
        clas = dl.askstring('Class', 'Enter Class').replace(' ', '')
        sect = dl.askstring('Sections', 'Enter sections (comma separated)').replace(' ', '')
        sub = dl.askstring('Subjects', 'Enter subjects (comma separated)').replace(' ', '')

        if be.class_add({clas: [sect, sub]}):
            be.store(8, 6)
            refresh()

    edit.add_command(label='Add Class', command=add)
    menubar.add_cascade(label='Edit', menu=edit)

    inspect = tk.Menu(menubar, tearoff=False)

    def dele():
        clas = dl.askstring('Class', 'Enter Class').replace(' ', '')
        sect = dl.askstring('Sections', 'Enter section').replace(' ', '')
        be.class_del(clas, sect)
        refresh()

    edit.add_cascade(label='Delete Class', command=dele)


def display(window, grd, sect):
    db.execute(f'select * from {grd}_{sect}')
    itable = db.fetchall()
    for widgets in window.winfo_children():
        if not repr(widgets).startswith('<tkinter.Menu object .!menu'):
            widgets.destroy()
    for i in range(len(itable)):
        for j in range(len(itable[0])):
            s = tk.StringVar()
            s.set(itable[i][j])
            tk.Entry(window, width=8, fg='blue',
                     font=('Comic Sans MS', 16, 'bold'), text=s, state=tk.DISABLED).grid(row=i, column=j)


if __name__ == '__main__':
    dbm = sq.connect(host='localhost', user='root', password='admin')
    dbm.autocommit = True
    db = dbm.cursor()

    root = tk.Tk()
    menubar = tk.Menu(root)

    root.title('TimeTable')

    menu(root)
    add_menu(root)

    root.mainloop()

