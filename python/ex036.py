casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos você deseja pagar? '))
prestaçao = casa /  (anos * 12)
minimo = salario * 30 / 100
print(f'O valor das pretações é de R${prestaçao :.2f}')
if prestaçao <= minimo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')
