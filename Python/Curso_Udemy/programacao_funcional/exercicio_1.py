# Vou começar defindo apenas meu salário

salario_base = 1550

def calcular_total_salario(salario):
    total_salario = salario
    horas_para_calcular = input("Insira as horas 60%:, 80%, 100% (Separados por vírgula): ") 
    x = horas_para_calcular.split(',')

    
    horasExtrasTratadas = []
    for numeros in x :
        horasExtrasTratadas.append(int(numeros))
    
    def calculo_horaExtra60(numero=7.18):
        saldo_horasExtras60 = horasExtrasTratadas[0] * numero
        return saldo_horasExtras60

    
    def calculo_horaExtra80(numero=1.80):
        saldo_horasExtras80 = horasExtrasTratadas[1] * numero
        return saldo_horasExtras80
    
    
    def calculo_horaExtra100(numero=9.16):
        saldo_horasExtras100 = horasExtrasTratadas[2] * numero
        return saldo_horasExtras100
    
    total_horasExtras = round((calculo_horaExtra60()+ calculo_horaExtra80() + calculo_horaExtra100()), 2)
    print(total_horasExtras)

    total_salario += total_horasExtras
    print(total_salario)
    
    somar_vale = 'N'
    vale_pego = input("O vale foi pego no meio do mês? [S] / [N]: ")
    if vale_pego == somar_vale:
        total_salario += 300
    else:
        total_salario += 0
    print(total_salario)

calcular_total_salario(salario_base)

        

