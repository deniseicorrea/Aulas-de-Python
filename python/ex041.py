from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano do seu nascimento? '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade < 9 :
    print('Classificaçao mirim')
elif idade > 9 and idade <= 14:
    print('Classifiçao infantil')
elif idade > 14 and idade <= 19:
    print('Classificaçao junior')
elif idade > 19 and idade <= 25:
    print('Classificaçao Senior')
else:
    print('Classificaçao master')