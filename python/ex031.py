distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor que você terá de pagar é R$ {valor :.2f}.')
else:
    valor = distancia * 0.45
    print(f'O valor que você terá de pagar é R$ {valor}.')