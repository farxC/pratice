from tkinter import *
import pandas as pd
import os
from tkinter import ttk
from janelaDois import enter_data

class Janela:
    def __init__(self, master, nome, idade, t_s, f):
        # Variaveis do usuario
        self.nome = nome
        self.idade = id
        self.t_s = t_s
        self.f = f

        # Pilares
        self.master = master
        self.main = Frame(self.master)
        self.main.configure()
        self.main.pack()

        # Alto
        self.top = Frame(self.main)
        self.title = Label(
            self.top, text="Bem vindo(a)! Insira aqui os exercícios propostos de cada dia.")
        self.title.pack(padx=10, pady=5)

        self.top.pack(pady=10)

        # Meio
        self.middle = Frame(self.main)

        df = pd.DataFrame(
            {
                 "Nome": [nome],
                  "Idade": [idade],
                 "Split de Treino": [t_s],
                    "Frequência": [f]
                 }
            )

        userDataView = ttk.Treeview(self.top)
        userDataView['columns'] = list(df.columns)
        userDataView.configure(height=1)

        for column in df.columns:
                userDataView.column(column, width=100, anchor=CENTER)
                userDataView.heading(column, text=column)
        for index, row in df.iterrows():
                userDataView.insert("", END, text=index, values=list(row))

        userDataView.pack()

        self.total_tables = 1
        self.total_rows = 8
        self.total_columns = 7

        self.cells = [[None for i in range(self.total_columns)]
                      for j in range(self.total_rows)]
        self.tables = []

        for x in range(self.total_tables):
            self.tables.append(Frame(self.middle))
            self.tables[x].pack()
            for i in range(self.total_rows):
                for j in range(self.total_columns):
                    if j == 0:
                        if i == 0:
                            self.cells[i][j] = Label(self.tables[x], text=' ')
                        else:
                            self.cells[i][j] = Label(
                                self.tables[x], text=f'Exercício {i}')
                            self.cells[i][j].grid(row=i, column=j)
                    elif i == 0:
                        self.cells[i][j] = Label(
                            self.tables[x], text=f'Treino {j}')
                        self.cells[i][j].grid(row=i, column=j)
                    else:
                        self.cells[i][j] = Entry(self.tables[x], width=30)
                        self.cells[i][j].grid(row=i, column=j)

        self.middle.pack(padx=10, pady=10)

        # Bottom Section
        # # Buttons section
        self.bottom = Frame(self.main)
        self.btnSave = Button(
            self.bottom, text="Salvar Log", command=self.save)
        self.btnSave.pack()
        self.bottom.pack(pady=15)

    def save(self):

        file = open("register.txt", "w")
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                if j != 0:
                    if i != 0:
                        file.write(self.cells[i][j].get()+'.')
                        print(self.cells[i][j])
                else:
                    pass

        file.close()

def run():
    janelaTerciaria = Tk()
    janelaTerciaria.geometry('1000x420')
    janela = Janela(janelaTerciaria,'Rafael',18, 'ABC', 4)
    janelaTerciaria.mainloop()

