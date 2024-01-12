
while True:
    try:
        print('Informe dois números')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        r = n1 / n2
        r2 = n1 + n2
        r3 = n1 - n2
        r4 = n1 * n2
        break
    except ValueError as e:
        print(e)
        print(f'Número inválidos! Tente novamente.')
    except ZeroDivisionError as e:
        print(e)
        print(f'Divisão por zero! Tente novamente.')

print(f'{n1} / {n2} = {r}')
print(f'{n1} + {n2} = {r2}')
print(f'{n1} - {n2} = {r3}')
print(f'{n1} X {n2} = {r4}')
