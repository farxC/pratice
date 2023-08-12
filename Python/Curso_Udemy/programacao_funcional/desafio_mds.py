from functools import reduce

def mdc(numeros):
    Min = min(numeros)
    print(int(Min))
    if Min % Min != 0:
        for x in range(1, Min):
            if Min % x == 0:
             return f'o Minimo Multiplo comum é {x}'
    


if __name__ == '__main__':
    print(mdc([21,7])) #7
    print(mdc([125, 40])) #5
    print(mdc([9,564, 66, 3])) # 3
    print(mdc([55,22])) # 11
    print(mdc([15,150])) # 15
    print(mdc([7,9]))  #1