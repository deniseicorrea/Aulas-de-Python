from random import randint
from time import sleep
computador = randint(0,5)
print('++_++'* 20)
print('Tente adivinhar um número entre 0 e 5')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, voce ganhou!!!')
else:
    print(f'Haha você perdeu!!! Eu pensei no número {computador}')