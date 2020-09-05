sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida, por favor informe o sexo corretamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')

