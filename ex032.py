from datetime import date

ano = int(input('Digite o ano (coloque 0 para ver o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano é bissexto')
else:
    print('Ano não é bissexto')
