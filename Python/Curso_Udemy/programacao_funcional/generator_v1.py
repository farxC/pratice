
def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'

def impar(elems):
    for i in elems:
        if i % 2:
            yield i



if __name__ == '__main__':
   

    for x in impar(range(20)):
        print(x)