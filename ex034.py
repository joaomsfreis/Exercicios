salario = float(input('Digite o salário: '))

if salario > 1250.0:
    salario = salario + (salario*10)/100
else:
    salario = salario + (salario*15)/100

print('Seu salário será {}'.format(salario))