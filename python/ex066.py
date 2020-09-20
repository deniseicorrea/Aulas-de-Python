cont = s = 0
while True:
    n = int(input('Digite um número:[999 Para parar] '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Ao todo foram digitados {cont} números e a soma entre eles é {s}')