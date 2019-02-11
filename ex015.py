km = float(input('Digite a quantidade de km percorridos: '))
dias = float(input('Digite a quantidade de dias: '))

print('O carro foi alugado durante {} dias e percorreu {} km, o valor a se pagar será de R${}!'.format(dias, km, dias*60.0+km*0.15))