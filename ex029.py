km = float(input('Digite a velocidade: '))

if km > 80.0:
    print('Você foi multado no valor de R$ {:.2f}'.format((km-80.0)*7.0))
else:
    print('Você não foi multado')
