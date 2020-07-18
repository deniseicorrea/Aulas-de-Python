frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frase.count("a")} vezes')
print(f'A letra A aparece pela primeira vez, na posiçao {frase.find("a")+1}')
print(f'A última letra aparece na posiçao {frase.rfind("a")+ 1}')