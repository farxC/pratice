from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class App(Tk):
    Janela = Tk()
    def janela_dados_usuario():
        segundaJanela= Tk()
        segundaJanela.geometry('300x900')

    def Confirm():
       confirmacao= messagebox.askquestion("Confirmação","Criar nova planilha? Você deverá responder algumas perguntas")
       if confirmacao == 'yes':
           print("Teste")
           
           
       else: 
           print('teste2')
    
    def menu():
        global Janela
        Janela= Tk()
        Janela.geometry("630x900")
        
        Janela.title('Programa de Treinamento')
        Janela.configure(bg=cor_fundo)
        Janela.state('zoomed')
        bg= Image.open('./mike.png')
        bck_end=ImageTk.PhotoImage(bg)  
        image_label = Label(Janela, image=bck_end).pack()
        text_boasvindas = "Hipertrofy Management "
        text_label = Label(Janela, text= text_boasvindas, 
                        bg="black",
                        fg='white').place(x=5,
                                        y=20)
        Janela.mainloop()        
    
   
    
    criar_novaPlanilha = Button(Janela, text= 'Crie uma nova planilha',
                                command= Confirm).place(relx =0.5, 
                                                            rely=0.92,anchor= 'center')
 
    Janela.mainloop()