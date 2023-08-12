class Humano:
    # Atributo de classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthanlensis'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('')