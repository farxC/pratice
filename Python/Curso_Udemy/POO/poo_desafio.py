from datetime import datetime

class Pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome;
        self.idade = idade;
    
    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome}: {self.idade} anos'

    def isAdult(self):
        if self.idade < MAIOR_IDADE:
            return f'{self.nome} não é maior de idade'
        else:
            return f'{self.nome} é maior de idade'


def get_data(compra):
    return compra.data

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []   
    
    def registrar_compra(self, compra):
       self.compras.append(compra)
       

    def get_data_ultima_compra(self):
        return None if not self.compras else \
        sorted(self.compras, key = get_data) [-1].data
    
    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total


class Compra(Cliente):
   def __init__(self, vendedor, data, valor):
       self.vendedor = vendedor
       self.data = data
       self.valor = valor



if __name__ == '__main__':
    pessoa1 = Pessoa('Rafael', 19)
    print(pessoa1)
    print(pessoa1.isAdult())

