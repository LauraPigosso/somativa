import tkinter
from threading import Thread
from tkinter import *
from tkinter.ttk import Combobox
from biblioteca import Magalu
from conexao import conexao, cursor
from tkinter import ttk

from inserir_livros import listar_livros, lista_livros_filtro


class Janela():

    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames()
        self.botao()
        self.lista_frame2()
        self.dropdown()
        self.select_list()
        self.janela.mainloop()

    def tela(self):  # cria a tela
        self.janela.title('Magalu')
        self.janela.configure(background='#fdfaf9')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame_1 = Frame(self.janela, bg='#7fc8f8')
        self.frame_1.place(relx=0.03, rely=0.10, relwidth=0.94, relheight=0.11)  # Criar cabeçario

        self.frame_2 = Frame(self.janela, bg='#7fc8f8', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_2.place(relx=0.03, rely=0.35, relwidth=0.94, relheight=0.55)  # Criar quadro de mostragem

    # Botão para atualizar
    def botao(self):
        self.btAtualizar = Button(self.frame_1, text="ATUALIZAR", command= self.Thread1)
        self.btAtualizar.place(relx=0.15, rely=0.28, relwidth=0.3, relheight=0.5)

        self.btAtualizar = Button(self.frame_1, text="ATUALIZAR", command=self.Thread1)
        self.btAtualizar.place(relx=0.15, rely=0.28, relwidth=0.3, relheight=0.5)

        self.btExport = Button(self.frame_1, text="EXPORTAR", height=2, width=13, command=self.open_win2)
        self.btExport.pack(side=LEFT, padx=10)

    # Quadro de mostragem
    def lista_frame2(self):
        self.listaLiv = ttk.Treeview(self.frame_2, height=3, columns=("", "editora", "nome", "preco"))
        self.listaLiv.heading('#0', text='')
        self.listaLiv.heading('#1', text='ID')
        self.listaLiv.heading('#2', text='Editora')
        self.listaLiv.heading('#3', text='Nome')
        self.listaLiv.heading('#4', text='Preço')

        self.listaLiv.column('#0', width=5)
        self.listaLiv.column('#1', width=35)
        self.listaLiv.column('#2', width=188)
        self.listaLiv.column('#3', width=188)
        self.listaLiv.column('#4', width=70)

        self.listaLiv.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        # Barra de Rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical', bg='#ffe45e')
        self.listaLiv.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.05, relwidth=0.04, relheight=0.9)

    def Thread1(self):
        t1 = Thread(target=self.Atualizar())
        t1.run()

    def Atualizar(self):  # atualizar a tabela de mostragem
        Magalu()

    def dropdown(self):  # Faz um menu de escolha de editoras para o usuario

        OPTIONS = ["apple", "galera", "record", "rocco", "compainha", "todos"]

        self.variable = StringVar(self.frame_1)
        self.variable.set(OPTIONS[0])
        self.popupMenu = Combobox(self.frame_1, textvariable=self.variable, values=OPTIONS)
        self.popupMenu.place(relx=0.53, rely=0.28, relwidth=0.3, relheight=0.5)
        self.popupMenu.bind('<<ComboboxSelected>>', lambda x: self.select_list_filtro(self.variable.get()))


    def select_list(self):
        self.listaLiv.delete(*self.listaLiv.get_children())
        for i in listar_livros():
            self.listaLiv.insert(parent='', index=0, values=i)

    def select_list_filtro(self, editoras):
        self.listaLiv.delete(*self.listaLiv.get_children())
        for i in lista_livros_filtro(editoras):
            self.listaLiv.insert(parent='', index=0, values=i)

   def expxlsx(self, formato):
       wb = Workbook()
       planilha = wb.active
       planilha.title = 'arquivo'

       aux = 1
       for item in self.lista["lista_editora"]:
           planilha[f'A{aux}'] = item
           aux += 1

       aux = 1
       for item in self.lista["lista_nomes"]:
           planilha[f'A{aux}'] = item
           aux += 1

       aux = 1
       for item in self.lista["lista_precos"]:
           planilha[f'B{aux}'] = item
           aux += 1

        wb.save('arquivo.xlsx')


def expcvs(self, formato):
    wb = Workbook()
    planilha = wb.active
    planilha.title = 'arquivo'

    aux = 1
    for item in self.lista["lista_editora"]:
        planilha[f'A{aux}'] = item
        aux += 1

    aux = 1
    for item in self.lista["lista_nomes"]:
        planilha[f'A{aux}'] = item
        aux += 1

    aux = 1
    for item in self.lista["lista_precos"]:
        planilha[f'B{aux}'] = item
        aux += 1

    wb.save('arquivo.cvs')


