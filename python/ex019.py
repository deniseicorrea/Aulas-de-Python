from random import choice
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O aluno sorteado é {escolhido}')
