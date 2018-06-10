# importando interface grafica e banco de dados

from tkinter import *
import sqlite3
import time

con = sqlite3.connect('database.db')
c = con.cursor()
sql = 'SELECT * FROM Users WHERE user = ?'
prd = 'SELECT * FROM Produtos WHERE id = ?'
c.execute('CREATE TABLE IF NOT EXISTS Users(user text, passw text, cargo text)')
c.execute('CREATE TABLE IF NOT EXISTS Produtos(id text, name text, valor text, quant text, val text)')
none = ('', '')
cad_none = ('', '', '', '', '')


# Menu

def cadastrar():
    id = et_id.get()
    name = et_name.get()
    price = et_price.get()
    quant = et_quant.get()
    val = et_val.get()
    cad = (id, name, price, quant, val)
    print(cad)
    c.execute("INSERT INTO Produtos (id, name, valor, quant, val) VALUES(?,?,?,?,?)", (id, name, price, quant, val))
    con.commit()
    lb_result['text'] = 'Cadastrado Com Sucesso!'
    lb_result['fg'] = 'green'

    '''
    if cad == cad_none:
        lb_result['text'] = 'Preencha os Formularios'
        lb_result['fg'] = 'red'
    else:
        c.execute("""
        SELECT * FROM Produtos;
        """)
        for id_prd in c.execute(prd, (id,)):
            if cad == id_prd:
                print('Ja tem')
            else:
                print('Nao tem')
                c.execute("INSERT INTO Produtos (id, name, valor, quant, validade) VALUES(?,?,?,?,?)", (id,name,price,quant,val))
                con.commit()
                lb_result['text'] = 'Cadastrado Com Sucesso!'
                lb_result['fg'] = 'green'
'''

def sistema():
    lb_user.grid(row=0,columnspan=2)
    menu_time.grid(row=1, columnspan=2)
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    bt4.destroy()
    print('OK')

def prod_cadastro():
    lb_user.grid(row=0,columnspan=2)
    menu_time.grid(row=1, columnspan=2)
    bt1['text'] = 'Cadastrar'
    bt1['command'] = cadastrar
    lb_result.grid(row=2, columnspan=2)
    lb_id.grid(row=3, column=0)
    lb_name.grid(row=4, column=0)
    lb_price.grid(row=5, column=0)
    lb_quant.grid(row=6, column=0)
    lb_val.grid(row=7, column=0)

    et_id.grid(row=3, column=1)
    et_name.grid(row=4, column=1)
    et_price.grid(row=5, column=1)
    et_quant.grid(row=6, column=1)
    et_val.grid(row=7, column=1)

    bt1.grid(row=8, columnspan=3)

    bt2.destroy()
    bt3.destroy()
    bt4.destroy()
    print('OK')

def estoque():
    print('OK')
    for estoque in c.fetchall():
        print(estoque)

def movimentacao():
    print('OK')

def menu():
    gui.title('Menu')
    lb_passw.destroy()
    lb_result['text'] = ''
    et_passw.destroy()
    bt_confirm.destroy()
    bt_register.destroy()
    user = et_user.get()
    et_user.destroy()
    lb_user['text'] = 'Bem Vindo "{}!"'.format(user)
    menu_time.grid(row=1, columnspan=2)
    bt1.grid(row=2, column=0)
    bt2.grid(row=2, column=1)
    bt3.grid(row=3, column=0)
    bt4.grid(row=3, column=1)

# Sair

def sair():
    exit()


# Sistema de Login

def cad_confirm():
    user = et_user.get()
    passw = et_passw.get()
    auth = (user, passw)

    if auth == ('', ''):
        lb_result['text'] = 'Preencha o Usuario e\n Senha Por Favor! :)'
        lb_result['fg'] = 'red'

    else:
        c.execute("INSERT INTO Users (user, passw, cargo) VALUES(?,?,?)", (user, passw, 'funcionario'))
        con.commit()
        lb_result['text'] = 'Cadastrado Com Sucesso!'
        lb_result['fg'] = 'green'
        sair()

def cad_login():
    user = et_user.get()
    passw = et_passw.get()
    auth = (user, passw, 'admin')
    auth1 = (user, passw)

    if none == auth1:
        lb_result['text'] = 'Preencha os Campos...'
        lb_result['fg'] = 'red'

    else:
        c.execute("""
        SELECT * FROM Users;
        """)

        for row in c.execute(sql, (user,)):
            hu3 = row

            if hu3 == auth:
                lb_result['text'] = 'Logado Com Sucesso!\n Digite novo User e Senha'
                lb_result['fg'] = 'green'
                et_user.delete(0, END)
                et_passw.delete(0, END)
                bt_confirm['command'] = cad_confirm
                bt_confirm['text'] = 'Cadastrar'

            else:
                lb_result['text'] = 'Usuario ou Senha Incorretos!'
                lb_result['fg'] = 'red'
                print('bug')


def login():
    user = et_user.get()
    passw = et_passw.get()
    auth = (user, passw)

    if auth == none:
        lb_result['text'] = 'Preencha os Campos...'
        lb_result['fg'] = 'red'

    else:
        c.execute("""
        SELECT * FROM Users;
        """)

        for row in c.execute(sql, (user,)):
            admin = ('admin', '123', 'admin')
            auth = (user, passw, 'funcionario')

            if row == admin:
                lb_result['text'] = 'Logado Com Sucesso!... Aguarde...'
                lb_result['fg'] = 'green'
                menu()

            else:
                if row == auth:
                    lb_result['text'] = 'Logado Com Sucesso!... Aguarde...'
                    lb_result['fg'] = 'green'
                    menu()

                else:
                    lb_result['text'] = 'Usuario ou Senha errados...\n Tente novamente'
                    lb_result['fg'] = 'red'


# Sistema de Cadastro

def register():
    lb_result['text'] = 'Antes de Cadastrar...\nVocê Deve Inserir um User Admin'
    lb_result['fg'] = 'red'
    bt_confirm['command'] = cad_login
    bt_register['command'] = sair
    bt_register['text'] = 'Sair'


# Criando interface de Login

gui = Tk()
gui.title('Faça o Login...')

lb_user = Label(gui, text='User: ')
lb_passw = Label(gui, text='passw: ')
lb_result = Label(gui, text='')

et_user = Entry(gui)
et_passw = Entry(gui, show='*')

bt_confirm = Button(gui, command=login, text='Login')
bt_register = Button(gui, command=register, text='Cadastrar')

menu_time = Label(gui, text='{}'.format(time.asctime()))

bt1 = Button(gui, command=sistema, text='Sistema')
bt2 = Button(gui, command=prod_cadastro, text='Cadastrar Produtos')
bt3 = Button(gui, command=estoque, text='Estoque')
bt4 = Button(gui, command=movimentacao, text='Movimentação')

lb_user.grid(row=0, column=0)
lb_passw.grid(row=1, column=0)
lb_result.grid(row=2, columnspan=2)

et_user.grid(row=0, column=1)
et_passw.grid(row=1, column=1)

bt_confirm.grid(row=3, columnspan=2)
bt_register.grid(row=4, columnspan=2)

lb_id = Label(gui, text='Codigo do produto:')
lb_name = Label(gui, text='Nome do produto:')
lb_price = Label(gui, text='Valor do produto:')
lb_quant = Label(gui, text='Quantidade do produto:')
lb_val = Label(gui, text='Validade do produto:')

et_id = Entry(gui)
et_name = Entry(gui)
et_price = Entry(gui)
et_quant = Entry(gui)
et_val = Entry(gui)

gui.mainloop()

'''
c.fetchall() >> Pesquisar TUDO





'''
