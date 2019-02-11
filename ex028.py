import random

numPC = random.randint(0, 5)
numUser = int(input('Digite um número de 0 à 5: '))

if numPC == numUser:
    print('Parabéns! O coputador escolheu {} e você {}.'.format(numPC, numUser))
else:
    print('Que pena! O coputador escolheu {} e você {}.'.format(numPC, numUser))
