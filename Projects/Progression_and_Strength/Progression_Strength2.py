from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


class App(Tk):
    # Definições do ambiente primário (Menu principal)
    cor_fundo = '#706f6f'
    janelaPrincipal = Tk()
    janelaPrincipal.state('zoomed')
    janelaPrincipal.title('Programa de Treinamento')
    janelaPrincipal.configure(bg=cor_fundo)
    janelaPrincipal.state('zoomed')
    bg = Image.open('./mike.png')
    bck_end = ImageTk.PhotoImage(bg)
    image_label = Label(janelaPrincipal, image=bck_end).pack()
    text_boasvindas = "Hipertrofy Management "
    text_label = Label(janelaPrincipal, text=text_boasvindas,
                       bg="black",
                       fg='white').place(x=5,
                                         y=20)

    def janela_Dados_Usuario():
        janelasecundaria = Tk()
        janelasecundaria.geometry('600x650')
        janelasecundaria.title('Registre seus dados')
        label_dados = Label(janelasecundaria, text="Antes de começarmos, registre alguns dados..").pack()


    def Confirm():
    
       confirmacao= messagebox.askquestion("Confirmação",
                                           "Criar nova planilha? Você deverá responder algumas perguntas")
       if confirmacao == 'yes':
           
           print("Teste")
           
           
       else: 
           print('teste2')

    criar_novaPlanilha = Button(janelaPrincipal, text='Crie uma nova planilha',
                                command=Confirm).place(relx=0.5,
                                                       rely=0.92, anchor='center')

    janelaPrincipal.mainloop()
