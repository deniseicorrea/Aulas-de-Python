from random import randint
computador = randint(0,10)
print('Eu pensei em um número, será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Número maior...Tente mais uma vez: ')
        elif jogador > computador:
            print('Número menor...Tente mais uma vez: ')

print(f'Parabéns, você acertou com {palpites} tentativas')