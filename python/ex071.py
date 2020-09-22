c50 = c20 = c10 = c1 = 0
print('=' * 30)
print('{:^30}'.format('BANCO DC'))
print('=' * 30)
valor = int(input('Qual o valor do saque? R$'))
total = valor
ced = 50
totced = 0
'''while valor >= 50:
    valor -= 50
    c50 +=1
while valor >= 20:
    valor -=20
    c20 +=1
while valor >= 10:       1° opçao(forma mais fácil)
    valor -=10
    c10 +1
while valor >= 1:
    valor -=1
    c1 +1
print(f'{c50} Notas de 50,00,{c20} Notas de 20,00,{c10} Notas de 10,00,{c1} Notas de 1,00')'''
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
         print(f'Total de {totced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
             ced = 1
        totced = 0
        if total == 0:
            break


