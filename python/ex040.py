n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média desse aluno é {media}')

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media < 7:
    print('Recuperaçao')
elif media >= 7.0:
    print('Aprovado')
