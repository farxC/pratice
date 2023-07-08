from tkinter import *
from tkinter import messagebox
import time


class Alarme:

    def __init__(self, master):
        self.master= master
        # Frame view
        self.main = Frame(self.master)

        self.main.pack(pady=30)
        self.title = Label(
            self.main, text='Registre o nome do cliente')
        self.title.pack()

        # Definição do tempo.
        self.hora = StringVar()
        self.minuto = StringVar()
        self.segundo = StringVar()

        # Setting by default 0
        self.hora.set("00")
        self.minuto.set("00")
        self.segundo.set("00")

        # Name frame (Top Frame)
        self.top = Frame(self.main)
        self.top.pack(pady=10)

        # Time Frame (Middle Frame)
        self.middle = Frame(self.main)
        self.middle.pack(pady=10)
        self.middleTitle = Label(
            self.middle, text="Tempo:").grid(row=0, column=1)
        # Entry's class to take a input from the user
        # This input's takes a name and time to register.
        self.nameEntry = Entry(self.top)
        self.nameEntry.pack()
        self.hourEntry = Entry(self.middle, width=3, font=(
            "Times New Roman", 18), textvariable=self.hora)
        self.hourEntry.grid(
            row=1, column=1)
        self.minuteEntry = Entry(self.middle, width=3, font=(
            "Times New Roman", 18), textvariable=self.minuto)
        self.minuteEntry.grid(
            row=1, column=2)
        self.secondEntry = Entry(self.middle, width=3, font=(
            "Times New Roman", 18), textvariable=self.segundo)
        self.secondEntry.grid(
            row=1, column=3)

        self.bottom = Frame(self.main)
        self.bottom.pack()

        self.Btn = Button(
            self.bottom, text='Registrar o cliente', command=self.submit)
        self.Btn.grid(row=0, column=0)

        self.labelClientes = Label(
            self.bottom, text='Clientes:')

    def submit(self):
        nome = self.nameEntry.get()

        temp = []
        temp.append(int(
            self.hora.get()) * 3600 + int(self.minuto.get()) * 60 + int(self.segundo.get()))

        clientes = [[nome], [temp]]

        self.labelClientes.grid(
            row=1, column=0)
        self.listarClientes = Label(
            self.bottom, text=nome)
        self.listarClientes.grid(
            row=2, column=0)

        self.tempoClienteCronometro = LabelFrame(
            self.bottom)
        self.tempoClienteCronometro.grid(
            row=2, column=1)
        print(list(temp))

        self.labelExcedido = Label(
            self.tempoClienteCronometro, text='TEMPO EXECIDIDO, PEDIR PREVISÃO N3')

        for i in range(len(temp)):
            while temp[i] > -1:
                mins, secs = divmod(
                    temp[i], 60)

                hours = 0

                if mins > 60:
                    hours, mins = divmod(
                        mins, 60)

                self.hora.set(
                    "{0:2d}".format(hours))
                self.minuto.set(
                    "{0:2d}".format(mins))
                self.segundo.set(
                    "{0:2d}".format(secs))

                self.master.update()
                time.sleep(1)

                if (temp[i] == 0):
                    self.labelExcedido.pack()
                    messagebox.showinfo(
                        "Timer zerado", "Mandar mensagem")

                temp[i] -= 1

main = Tk()
main.geometry('400x400')
main2 = Tk()
main2.geometry('400x400')
a = Alarme(main)
b = Alarme(main2)
main.mainloop()
main2.mainloop