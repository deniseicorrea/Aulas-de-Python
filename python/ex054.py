from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasc = int(input(f'Ano de nascimento da {c}° pessoa? '))
    idade = atual - nasc
    if idade >=  21:
       totmaior += 1
    else:
       totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'E ao todo tivemos {totmenor} menores de idade')


