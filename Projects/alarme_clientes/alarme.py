from tkinter import *
import time
from tkinter import messagebox



class Temporizador:
    def __init__(self, master):
        self.master = master

        self.main = Frame(self.master)

        self.main.pack(pady=30)
        self.title = Label(
            self.main, text= "Temporizador de clientes!"
        )
        self.title.pack()

        # Top Frame Window
        self.top= Frame(self.main)
        self.top.pack(pady=10)

        # Middle Frame

        self.middle = Frame(self.main)
        self.middle.pack(pady=10)

        # Bottom Frame

        self.bottom = Frame(self.main)
        self.bottom.pack(pady=10)


        frameRegistrar = LabelFrame(self.bottom)
        frameRegistrar.pack()
        btnEnviar = Button(frameRegistrar, text='Registrar', command=self.submit)
        btnEnviar.pack()

       

    def Clientes(self):
        frameClientes = LabelFrame(self.top)
        frameClientes.pack()
        labelInserir = Label(frameClientes, text='Registre o nome do cliente:')
        labelInserir.pack()
        self.nomeCliente = Entry(frameClientes, font='18')
        self.nomeCliente.pack()
    
    def Alarme(self):
        valoresLabel = Label(self.middle, text= 'Pré-definições de alarme:')
        valoresLabel.pack()
        frameAlarme = LabelFrame(self.middle)
        frameAlarme.pack()

        self.v= IntVar()
        
        self.hora = StringVar()
        self.minuto = StringVar()
        self.segundo = StringVar()
       
        def presets():
            
            umaHora = Radiobutton(frameAlarme, text="1 Hora",variable=self.v, value=1)
            umaHora.pack()
            duasHoras = Radiobutton(frameAlarme, text="2 Horas",variable=self.v,value=2)
            duasHoras.pack()
            outraOpcao = Radiobutton(frameAlarme, text="Outro:", variable=self.v,value=3, command=lambda: other(self.v.get()))
            outraOpcao.pack()

        def other(valor):
            
            if valor == 3:    
                
                # Setting default 0
                self.hora.set("00")
                self.minuto.set("00")
                self.segundo.set("00")

            
                frameDefinirEspecifico = LabelFrame(self.middle)
                frameDefinirEspecifico.pack()
                horaLabel = Label(frameDefinirEspecifico, text='H:')
                horaLabel.grid(row=1, column=1)
                horaEntry = Entry(frameDefinirEspecifico, width=3, textvariable= self.hora, font=('Times New Roman', 18))
                horaEntry.grid(row=1, column=2)
                
                minutoLabel = Label(frameDefinirEspecifico, text='M:')
                minutoLabel.grid(row=1, column=3)
                minutoEntry = Entry(frameDefinirEspecifico, width=3, textvariable=self.minuto, font=('Times New Roman', 18))
                minutoEntry.grid(row=1, column=4)

                segundoLabel = Label(frameDefinirEspecifico, text='S:')
                segundoLabel.grid(row=1, column=5)
                segundoEntry = Entry(frameDefinirEspecifico, width=3, textvariable= self.segundo, font=('Times New Roman', 18))
                segundoEntry.grid(row=1, column=6)
                
               
              
            
        presets()
    def submit(self):
        nome = self.nomeCliente.get()       
        temp = 0
        
        if self.v.get() == 1:
           temp = 3600
            
        elif self.v.get() == 2:
            temp = 3600 * 2
            print(temp)
        else:
           temp = int(self.hora.get()) * 3600 + int(self.minuto.get()) * 60 + int(self.segundo.get())
            
        frameRegistros = Frame(self.bottom)
        frameRegistros.pack()
       

        labelNome = Label(frameRegistros, text=nome)
        labelNome.grid(row=1, column=0)
        
        frameCronometro = LabelFrame(frameRegistros)
        frameCronometro.grid(row=1, column=1)

        h = StringVar()
        m = StringVar()
        s = StringVar()

        entryHora = Entry(frameCronometro, width=3, textvariable= h).grid(row=0, column=0)
        entryMinuto = Entry(frameCronometro, width=3, textvariable= m).grid(row=0, column=1)
        entrySegundo = Entry(frameCronometro, width=3, textvariable= s).grid(row=0, column=2)
        
        def iniciar(temp):
            for i in range(temp):
                while temp > -1:
                    mins, secs = divmod(
                        temp, 60
                    )
                    hours = 0

                    if mins > 60:
                        hours, mins = divmod(
                            mins, 60
                        )

                    h.set("{0:2d}".format(hours))
                    m.set("{0:2d}".format(mins))
                    s.set("{0:2d}".format(secs))

                    self.master.update()
                    time.sleep(1)    

                    if (temp==0):
                        messagebox.showinfo("Zerado", f'Tempo excedido para o cliente {nome}!')

                    temp -= 1    
        iniciar(temp)
        
        


       

main = Tk()
main.geometry('400x400')
main.title("Alarme de clientes")
b = Temporizador(main)
b.Clientes()
b.Alarme()


main.mainloop()


