from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' *11)
print(f'Computador jogou a opçao {itens[computador]}')
print(f'Jogador jogou a opçao {itens[jogador]}')
print('-=' * 11)
if computador == 0:
   if jogador == 0:
      print('Empate')
   elif jogador == 1:
      print('Jogador vence')
   elif jogador == 2:
      print('Computador vence')
   else:
       print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
       print('Computador vence')
    elif jogador == 1:
       print('Empate')
    elif jogador == 2:
       print('Jogador vence')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
       print('Jogador vence')
    elif jogador == 1:
       print('Computador vence')
    elif jogador == 2:
       print('Empate')
    else:
        print('Jogada inválida')