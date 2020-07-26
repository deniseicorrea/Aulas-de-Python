from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual- nasc
print(f'Voce tem {idade} anos')
if idade == 18:
    print('Você tem que se alistar Imediatamente')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Você ainda não precisa se alistar, ainda faltam {saldo} anos.')
    print(f'Você se alistará no ano {ano}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado a {saldo} anos.')
    print(f'Você deveria ter se alistado no ano {ano}')