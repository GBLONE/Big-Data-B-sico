
def juros(capital, taxa, tempo=12):
    return (capital * taxa * tempo) / 100

print('Cálculo de Juros')
cap = float(input('Capital: '))
tax = float(input('Taxa: '))
tem = input('Tempo (deixe em branco para o padrão 12): ')

if tem == '':
    jur = juros(cap, tax)
else:
    tem = float(tem)
    jur = juros(taxa=tax, capital=cap, tempo=tem)
print(f'O valor dos juros é {jur}')
# pg 48