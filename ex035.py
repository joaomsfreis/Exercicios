print('\033[7;34mVerifica triângulo\033[m')
l1 = float(input('Digite o valor de um lado: '))
l2 = float(input('Digite o valor de um lado: '))
l3 = float(input('Digite o valor de um lado: '))

if abs(l1-l2) < l3 and abs(l1-l3) < l2 and abs(l3-l2) < l1 and l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')
