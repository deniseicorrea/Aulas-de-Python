preço = float(input('Digite o preço do produto:R$ '))
novo = preço-(preço * 5/100)
print(f'O produto de R${preço :.2f}, agora custará R$ {novo :.2f}')