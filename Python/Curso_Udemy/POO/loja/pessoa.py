MAIOR_IDADE = 18

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
class Vendedor(Pessoa):
    def __init__ (self, nome, idade, salario):
       super().__init__(nome, idade)
       self.salario = salario