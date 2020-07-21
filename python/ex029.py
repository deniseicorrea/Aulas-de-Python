velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você excedeu o limite.')
    multa = (velocidade-80)*7
    print(f'Voce foi  multado a um valor de R${multa}')
print('Tenha um bom dia!!!')