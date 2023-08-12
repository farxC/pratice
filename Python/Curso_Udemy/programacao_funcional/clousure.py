def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular # Aqui a função MULTIPLICAR __RETORNA__ a função calcular

if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print(dobro)
    print(triplo)
    print(f'O triplo de 3 é {triplo(3)}')