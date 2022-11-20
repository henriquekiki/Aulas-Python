# Conversor de Dolar para Real

a = float(input('Quantos dolares quer converter?: '))
b = float(input('Qual a cotação do dia?: '))

reais = (a * b)

print('Convertidos, fica: {} R$'.format(reais))


c = str(input('Quer fazer uma nova cotação?\nDigite sim ou não: '))

while c == 'sim':
    a = float(input('Quantos dolares quer converter?: '))
    b = float(input('Qual a cotação do dia?: '))

    reais = (a * b)

    print('Convertidos, fica: {} R$'.format(reais))

    c = str(input('Quer fazer uma nova cotação?\nDigite sim ou não: '))

else:
    print('OK.\nAté logo!')
