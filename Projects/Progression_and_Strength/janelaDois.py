from tkinter import *
from janelaTres import *



class janela_Dados:
    # Configurações janela de registro
    def __init__(self, master):
        self.master = master
        self.main = Frame(self.master)
        self.main.configure(bg= '#515151')
        self.main.pack()

         # Dados primários Frame
        self.DP_frame = Frame(self.main, )
        self.DP_frame.pack(pady=25)
        
        
        #Informações do usuário 
        self.label_dados = LabelFrame(
            self.DP_frame, text="Registre alguns dados pessoais", font='bold 8')
        self.label_dados.grid(row= 0, column=0)
        self.label_dados.configure(pady=10,bg='#6a6a6a', fg='white')
        

        # Definindo variáveis primárias 
        self.nome_do_usuario = Label(self.label_dados, text="Fale seu nome completo", bg="#2F3332", fg='white')
        self.nome_do_usuario.grid(row=0, column=0)
        self.idade_do_usuario = Label(self.label_dados, text="Insira sua idade",bg="#2F3332", fg='white')
        self.idade_do_usuario.grid(row= 0, column= 1)


        self.nome_do_usuario_entry = Entry(self.label_dados)
        self.nome_do_usuario_entry.grid(row=1, column= 0)
        self.idade_do_usuario = Spinbox(self.label_dados, from_= 6, to=80)
        self.idade_do_usuario.grid(row=1,column=1)

        # Dados de treinamento Frame
        self.TR_frame= Frame(self.main)
        self.TR_frame.pack(pady=25)

        # Informações sobre o treinamento do usuário
        self.label_dados_treinamento = LabelFrame(
            self.TR_frame, text="Antes de criar a planilha, informe alguns dados sobre sua rotina de treinamentos", font='bold 8')
        self.label_dados_treinamento.grid(row=0, column= 0)
        self.label_dados_treinamento.configure(pady=10, bg='#6a6a6a', fg='white')

        # Definindo variáveis de treinamento
        self.quantd_vzs_treina = Label(self.label_dados_treinamento, text="Quantas vezes você treina na semana?", bg="#2F3332", fg='white')
        self.quantd_vzs_treina.grid(row=0, column= 0)
        self.getquantd_vzs_treina = Entry(self.label_dados_treinamento)
        self.getquantd_vzs_treina.grid(row=0, column= 1)
        self.training_split= Label(self.label_dados_treinamento, text="Qual é seu split de treino?", bg="#2F3332", fg='white')
        self.training_split.grid(row=1, column=0)
        self.getTraining_split = Entry(self.label_dados_treinamento)
        self.getTraining_split.grid(row=1, column=1)

        for widget in self.label_dados.winfo_children():
            widget.grid_configure(padx= 10, pady= 3)
        for widget in self.label_dados_treinamento.winfo_children():
            widget.grid_configure(padx= 5, pady= 4)
        # Enviar dados
        self.button = Button(self.main, text="Registrar dados", command= self.enter_data)
        self.button.pack(pady=25)

        

        

    def enter_data(self):
        
        #User Info
        nome = self.nome_do_usuario_entry.get()
        idade= self.idade_do_usuario.get()

        # Training Info
        frequency = self.getquantd_vzs_treina.get()
        training_split = self.getTraining_split.get()
        print(nome)
        return nome, idade, frequency, training_split    


def win():
    
    janelasecundaria = Tk()
    janelasecundaria.geometry('600x400')
    janelasecundaria.title('Registre seus dados')
    janelasecundaria.configure(bg='#383838')

    a = janela_Dados(janelasecundaria)
    
    janelasecundaria.mainloop()


win()