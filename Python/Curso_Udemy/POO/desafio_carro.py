class Carro:
    def __init__(self, velocidadeMax):
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual= 0

    def acelerar(self, delta =5):
        maxima = self.velocidadeMax
        novaVelocidade = self.velocidadeAtual + delta
        self.velocidadeAtual = novaVelocidade if novaVelocidade <= maxima else maxima
        return self.velocidadeAtual
    
    def frear(self, delta =5):
        novaVelocidade = self.velocidadeAtual - delta
        self.velocidadeAtual = novaVelocidade if novaVelocidade >= 0 else 0
        return self.velocidadeAtual
if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(20):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))