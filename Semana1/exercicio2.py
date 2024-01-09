
nome = input('Informe o nome do aluno: ').upper()
nota = float(input('Informe a nota: '))

if nota >= 60:
    print(f'Aprovado(a)! Parabéns {nome} sua nota foi {nota}pts.')
    print(f'Boas Férias!')
else:
    if nota >= 40:
        print(f'Prezado(a) {nome}, você está de recuperação!')
        print(f'Sua nota foi {nota}pts.')
    else:
        print(f'Reprovado! Por favor aluno(a) {nome}, chame seus pais.')
        print(f'Sua nota: {nota}pts.')

