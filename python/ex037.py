num = int(input('Digite um número inteiro: '))
print(''''Escolha uma das bases para conversão:
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''''')
opçao = int(input('Escolha sua opçao: '))
if opçao == 1:
    print(f'Convertido para binário é {bin(num)[2:]}')
elif opçao == 2:
    print(f'Convertido para octal é {oct(num)[2:]}')
elif opçao == 3:
    print(f'Convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Opçao inválida')
