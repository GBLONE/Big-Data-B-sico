import math

print('Informe os termos da equação  Ax² + Bx +C:')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a == 0:
    print('Não é uma equação de segundo grau.')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('A equação não tem raízes')
    elif delta == 0:
       x1 = b * (-1)/2 * a
       print(f'A equação possuí a raíz: {x1}')
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (b * (-1) + raiz_delta)/ 2 * a
        x2 = (b * (-1) - raiz_delta)/ 2 * a
        print(f'A equação possuí duas raízes: ')
        print(f'X1 = {x1}')
        print(f'X2 = {x2}')