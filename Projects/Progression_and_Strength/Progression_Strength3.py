from tkinter import *
from tkinter import ttk
from janelaDois import win
from tkinter import messagebox
from PIL import ImageTk, Image


# Configuração do ambiente primário


cor_fundo = '#706f6f'
janelaPrincipal = Tk()
janelaPrincipal.state('zoomed')
janelaPrincipal.title('Programa de Treinamento')
janelaPrincipal.configure(bg=cor_fundo)
janelaPrincipal.state('zoomed')
janelaPrincipal.iconbitmap(r'arnold.ico')
bg = Image.open('./mike.png')
bck_end = ImageTk.PhotoImage(bg)
image_label = Label(janelaPrincipal, image=bck_end).pack()
text_label = Label(janelaPrincipal, text="Hipertrofy Management ",
                      bg="black",
                      fg='white',
                      font='Lexend 15 bold').place(x=5,
                                         y=20)


def Confirm():

        confirmacao = messagebox.askquestion("Confirmação",
                                             "Criar novo log? Você deverá responder algumas perguntas")
        if confirmacao == 'yes':    
            janelaPrincipal.destroy()     
            win()
            
            
criar_novaPlanilha = Button(janelaPrincipal, text='Criar log',
                                command=Confirm).place(relx=0.37,
                                                       rely=0.92, anchor='center')

abrir_planilhas = Button(janelaPrincipal, text='Acesse logs').place(
      relx=0.63, rely=0.92, anchor='center')

janelaPrincipal.mainloop()

