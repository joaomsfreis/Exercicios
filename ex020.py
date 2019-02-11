import random

alunos = []
ordem = []
val = 0

for i in range(4):
    alunos.append(input('Digite o nome do aluno {}: '.format(i + 1)))

random.shuffle(alunos) #Embaralha listas
print(alunos)
