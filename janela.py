from tkinter import *
from conexao import conexao, cursor
from tkinter import ttk

janela = Tk()


class Janela:
    def __init__(self):
        self.janela = janela
        self.tela()

    def tela(self):
        self.janela.title('Magalu')
        self.janela.configure(background='#bdbcb3')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)


Janela()
