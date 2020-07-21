from datetime import date
ano = int(input('Digite o ano que quer analizar ou digite O para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('ANO BISSEXTO')
else:
    print('NÃO É BISSEXTO')