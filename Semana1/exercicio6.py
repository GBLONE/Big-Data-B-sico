print('Multiplicação')
numero1 = int(input('Primeiro Numero : '))
numero2 = int(input('Segundo Numero: '))

resultado = 0
contador = 0

while True:
    if contador < numero2:
        resultado = resultado + numero1
        contador = contador + 1
    else:
        print(resultado)
        break