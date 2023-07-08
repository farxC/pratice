

#Só para ajudar o amigo. Obrigado pelas aulas.

from tkinter import *

import time

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#Configurando janela
janela = Tk()
janela2 = Tk()
janela.title("")
janela.geometry("385x180")
janela2.geometry("385x180")
janela.config(bg=cor1)
janela2.config(bg=cor1)
janela.resizable(width=FALSE,height=FALSE)

#Variaveis globais
global h
global m
global s
global limite
global start

#variaveis
tempo="00:00:00"
limite=59
liga=False
start=True
h=0
m=0
s=0

#Função contador
def contador():
    if (liga):
        global limite
        global h
        global m
        global s

        s+=1
        tempo=str("{:02d}:{:02d}:{:02d}".format(h,m,s))
        label_tempo["text"]=tempo
        if (m==limite and s==limite):
            s=-1
            m=0
            h+=1
        if (s == limite):
            s=-1
            m+=1
        label_tempo.after(1000,contador)
 
def start():
    global liga
    global start
    start=False
    if (liga):
        pass
    else:
        liga = True
        contador()
     
def pause():
    global liga
    liga=False

def reiniciar():
    global liga
    global h
    global m
    global s
    global start
    if (start):
        pass
    else:
        if(liga):
            h=0
            m=0
            s=-1
            label_tempo["text"]="00:00:00"
        else:
            h=0
            m=0
            s=-1
            label_tempo["text"]="00:00:00"
            liga=True
            contador()

def zerar():
    global liga
    global h
    global m
    global s
    h=0
    m=0
    s=0
    liga=False
    label_tempo["text"]="00:00:00"
    
#Criando labels
label_app = Label(janela,text="cronômetro",font=("Areal 10"),bg=cor1,fg=cor2)
label_app.place(x=20,y=5)

label_tempo = Label(janela,text=tempo,font=("Time 40 bold"),bg=cor1,fg=cor3)
label_tempo.place(x=60,y=30)

#Criando botões
botao_iniciar = Button(janela,command=start,text="Iniciar",width=7,height=2,bg=cor1,fg=cor2,font="Ivy 8 bold",relief="raised",overrelief="raised")
botao_iniciar.place(x=20,y=130)

botao_pausar = Button(janela,command=pause,text="Pausar",width=7,height=2,bg=cor1,fg=cor2,font="Ivy 8 bold",relief="raised",overrelief="raised")
botao_pausar.place(x=110,y=130)

botao_reiniciar = Button(janela,command=reiniciar,text="Reiniciar",width=7,height=2,bg=cor1,fg=cor2,font="Ivy 8 bold",relief="raised",overrelief="raised")
botao_reiniciar.place(x=200,y=130)

botao_zerar = Button(janela,command=zerar,text="zerar",width=7,height=2,bg=cor1,fg=cor2,font="Ivy 8 bold",relief="raised",overrelief="raised")
botao_zerar.place(x=290,y=130)


janela.mainloop()
janela2.mainloop()