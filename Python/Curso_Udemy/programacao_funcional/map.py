list_1 = [1,2,3]

dobro = map(lambda x: x * 2, list_1)

print(list(dobro))

list_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 25}
]

apenas_nomes = map(lambda y: y['nome'], list_2)

apenas_idade = map(lambda y: y['idade'], list_2)

print('Apenas idades:', list(apenas_idade))
print('Apenas nomes:', list(apenas_nomes))


list_3 = [
    {'nome': 'Rafael', 'idade': 19, 'salario': 1550},
    {'nome': 'Nathan', 'idade': 18, 'salario': 1350},
    {'nome': 'Brunno', 'idade': 24, 'salario':3000},
    {'nome': 'Guilherme', 'idade': 21, 'salario': 1300},
    {'nome': 'Jairo', 'idade': 20, 'salario': 900},
]


calculando_horas = map (lambda y: y['salario'] * 0.2 + y['salario'], list_3)

print('Calculo básico:', list(calculando_horas))


def calc_horas(self):
    calculos_horas_100 = map(lambda y: y['salario'] * 0.5)
