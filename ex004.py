text = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(text)))
print('Só tem espaço? {}'.format(text.isspace()))
print('É um número? {}'.format(text.isnumeric()))
print('É alfabético? {}'.format(text.isalpha()))
print('É alfanumérico? {}'.format(text.isalnum()))
print('Está em maiúsculo? {}'.format(text.isupper()))
print('Está em minusculo? {}'.format(text.islower()))
print('É capitalizada? {}'.format(text.istitle()))
