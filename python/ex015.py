km = float(input('Quantos quilometros foram percorridos? '))
dias = int(input('Quantos dias de aluguel? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar pelo aluguel é de R${pago :.2f}')
