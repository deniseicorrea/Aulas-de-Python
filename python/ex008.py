medida = float(input('Distancia em metros: '))
km = medida/ 1000
hm = medida/ 100
decm = medida/ 10
dc = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida {medida} corresponde {km} kilometros, {hm} hectometros, {decm} decametros,')
print(f'a {dc} decimetro, {cm :.0f} centimetros e {mm :.0f} milímetros')
