import math

n = float(input('Informe um número: '))
x = n * math.pi

print(f'x = n * pi = {n}')
print(f'Teto de x = {math.ceil(x)}')
print(f'Piso de x = {math.floor(x)}')
print(f'Log de x na base 10 = {math.log(x, 10)}')
print(f'Raíz de x = {math.sqrt(x)}')
