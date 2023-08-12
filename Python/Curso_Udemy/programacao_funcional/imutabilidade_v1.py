
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')


# Listar todos os meses do ano com 31 dias
# Listar todos os meses do ano com 31 dias
# 1. Pegar os indices de todos os meses com 31 dias 
# 2. (map) transformar os índices em nome 
# 3. (Reduce) juntar tudo para imprimir

apenas_31 = filter(lambda mes: mdays[mes] == 31  , range(1, 13))

transformar_nome = map(lambda nome: month_name[nome], apenas_31)

juntar_meses = reduce (lambda tudo, nome_mes: f'{tudo} \n- {nome_mes}', transformar_nome, 'Meses com 31 dias: ' )

print(juntar_meses)
