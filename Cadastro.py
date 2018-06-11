import sqlite3
from tkinter import *
con = sqlite3.connect('database.db')
c = con.cursor()

def cadastro():
    user = et1.get()
    passw = et2.get()
    auth = (user,passw)
    admin = 'admin'
    c.execute('CREATE TABLE IF NOT EXISTS Users(user text,passw text,cargo text)')
    c.execute("INSERT INTO Users (user,passw,cargo) VALUES(?,?,?)",(user,passw,admin))
    con.commit()
    print('Sucesso!')

tk_cadastro = Tk()
lb1 = Label(tk_cadastro,text = 'User ')
lb2 = Label(tk_cadastro,text = 'Senha ')
et1 = Entry(tk_cadastro)
et2 = Entry(tk_cadastro,show='*')
bt1 = Button(tk_cadastro,text = 'Cadastrar!',command = cadastro)
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
et1.grid(row=0, column=1)
et2.grid(row=1, column=1)
bt1.grid(row=3, columnspan=2)
tk_cadastro.title('Cadastrar!')
tk_cadastro.mainloop()
