frase = str(input('Digite algo: ')).upper().strip()
print('Numeros de A: {}'.format(frase.count('A')))
print('Primera posição de A: {}'.format(frase.find('A')+1))
print('Ultima posição de A: {}'.format(frase.rfind('A')+1))
