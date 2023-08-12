class Pessoa:
    def __init__ (self, nome, idade, estadoCivil, dinheiroHora):
        self.nome = nome
        self.idade = idade
        self.estadoCivil = estadoCivil
        self.dinheiroHora = dinheiroHora

    
    def situacaoAmorosa(self):   
        if self.estadoCivil=='solteiro':
            return f'{self.nome} man vc ta solteiro'
        elif self.estadoCivil=='casado':
            return f'{self.nome} man vc ta casado'
        elif self.estadoCivil== 'namorando':
            return f' {self.nome} man termina isso k'
        else:
            return 'vc eh doido'
    
    def dinheiroNaConta(self):
        dinheiroTotal = 0
        for _ in range (6):
            dinheiroTotal += self.dinheiroHora 
        return dinheiroTotal


        
pessoa1 = Pessoa('Rafael', 18 , 'namorando', 10)
print(pessoa1.situacaoAmorosa())
print(pessoa1.dinheiroNaConta)


