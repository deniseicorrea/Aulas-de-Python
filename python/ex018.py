from math import radians, sin , cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O seno do ângulo é {seno :.2f}')
cos = cos(radians(angulo))
print(f'O cosseno desse número é {cos :.2f}')
tan =tan(radians(angulo))
print(f'O valor da tangente é {tan :.2f}')