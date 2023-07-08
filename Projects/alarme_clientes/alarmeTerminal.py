import time
from tkinter import messagebox
def Cliente():
    global nome
    global tempo
    nome = input("Digite o nome do cliente:\n")
    tempo = input("Digite o tempo, nesse formato H/M/S:")
    t = tempo.split('/')

    def Temporizador():
        
        for i in range(len(t)):
            t[i]= int(t[i])
        tempoTotal = t[0] * 3600 + t[1] + t[2] 
        segundos = t[2] % 60
        minutos = t[1]
        horas = t[0] 
        

        for x in range(tempoTotal, 0, -1):
            print(f"H:{horas-x:2d}/M:{minutos-x:2d}/:{segundos-x:2d}")
            time.sleep(1)
            if tempoTotal == 0:
                print("Tempo encerrado ")
            
           
            

    Temporizador()
    


Cliente()
