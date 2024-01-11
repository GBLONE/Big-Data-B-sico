print('Informe dois números: ')
n1 = int(input('N1: '))
n2 = int(input('N2: '))

if n1 < 1 or n2 < 1:
    print('Números inválidos para MDC')
else:
    while True:
        resto = n1 % n2
        print(f'{n1} / {n2} -> resto: {resto}')
        if resto == 0:
            break
        n1 = n2
        n2 = resto
        print(f'O MDC é: {n2}')