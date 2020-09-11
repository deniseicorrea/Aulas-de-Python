numero = cont = soma = 0
numero = int(input('Digite um número [999 para PARAR]: '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um número [999 para PARAR]: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
