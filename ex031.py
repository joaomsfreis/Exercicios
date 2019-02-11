km = float(input('Digite a distância da viagem: '))

if km > 200.0:
    print('O valor da passagem é R${:.2f}!'.format(km*0.45))
else:
    print('O valor da passagem é R${:.2f}!'.format(km*0.5))
