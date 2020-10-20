from utilities import func
from utilities import textos
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()
        self.titulo = Label(self.primeiroContainer, text='Sistema Bar')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['width'] = 500
        self.segundoContainer.pack(side=RIGHT)
        self.mesas = Label(self.segundoContainer, text='Mesas abertas')
        self.mesas['font'] = self.fontePadrao
        self.mesas.pack(side=LEFT)
        self.hello = Label(self.segundoContainer, text='hello')
        self.hello.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(side=LEFT)
        self.teste = Label(self.terceiroContainer, text='SEi la')
        self.teste['font'] = self.fontePadrao
        self.teste.pack()



root = Tk()
root.title('Sistema Bar')
root.geometry('500x500+500+100')
Application(root)
root.mainloop()



"""
janela = tkinter.Tk()
janela.title('Sistema Bar')
janela.geometry('500x500+500+100')
janela.resizable(False, False)
janela.iconbitmap('/Users/Matheus/Desktop/Tkinter/icon.ico')

btn1 = tkinter.Button(janela, text = 'Abrir mesa', command=lambda: func.abrir_mesa())
btn1.pack()

btn2 = tkinter.Button(janela, text = 'Deletar mesa', command=lambda: func.deletar_mesa())
btn2.pack()

btn3 = tkinter.Button(janela, text = 'a', command=lambda: print('a'))
btn3.pack()

janela.mainloop()
"""