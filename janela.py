from tkinter import *
from conexao import conexao, cursor
from tkinter import ttk



class Janela:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.janela.mainloop()
        self.frames()

    def tela(self):
        self.janela.title('Magalu')
        self.janela.configure(background='#fff')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame0 = Frame(self.janela, bg='#E8AEB7')
        self.frame0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)




Janela()
