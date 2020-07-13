'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente:'))
hi = (co**2 + ca**2) ** (1/2)
print(f'a hipotenusa vai medir {hi :.2f}')'''
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente:'))
hi = hypot(co,ca)
print(f'a hipotenusa vai medir {hi :.2f}')

