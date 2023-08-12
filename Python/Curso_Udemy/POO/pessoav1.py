#-*-coding: UTF-8
class Pessoa:
    def set_details(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def returning_details(self):
        print('Olá ', self.nome, 'você possui ', self.idade, 'anos' )

pessoa1 = Pessoa()
pessoa1.set_details('Rafael', 19)
pessoa1.returning_details()