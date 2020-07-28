print('{:=^40}'.format(' Lojinha da Giu '))
preço = float(input('Valor da compra: R$ '))
print('''FORMA DE PAGAMENTO
[1] A vista/dinheiro ou cheque
[2] á vista cartão
[3] 2X no cartão
[4] 3X ou mais no cartão''')
opçao = int(input('Qual é a opçao? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)

elif opçao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra parcelada em 2X de R$ {parcela :.2f}')
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totalpac = int(input('Quantas parcelas? '))
    parcela = total / totalpac
    print(f'Sua compra parcelada em {totalpac} vezes de R${parcela :.2f}')
else:
    total = preço
    print('\033[31mOpção inválida\033[m')

print(f'Sua compra vai custar R$ {total :.2f}')
