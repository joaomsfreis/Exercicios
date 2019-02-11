nome = str(input('Digite um nome: ')).strip()

print('Primero nome: {}'.format(nome[:nome.find(' ')]))
print('Primero nome: {}'.format(nome[nome.rfind(' ')+1:]))
