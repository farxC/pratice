from functools import reduce

pessoas = [ 
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

# Reduce é uma função que pode gerar uma outra lista (como todos os outros manipuladores de conjuntos)

menores = filter(lambda p: p['idade'] < 18, pessoas)


soma_idades = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades)
