import random

alunos = []

for i in range(4):
    alunos.append(input('Digite o nome do aluno {}: '.format(i+1)))

print('O aluno escolhido foi: {}'.format(random.choice(alunos))) #Escolhe um valor de uma lista


