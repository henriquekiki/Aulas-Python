def calculadora_dias():
    from datetime import date
    hoje = date.today()
    hoje_str = hoje.strftime('%d/%m/%Y')
    print(hoje_str)

    ano = int(input('Qual o ano que você nasceu: '))
    mes = int(input('Qual o mes que você nasceu: '))
    dia = int(input('Qual o dia que você nasceu: '))
    nascimeto = date(ano, mes, dia)
    nascimeto_str = nascimeto.strftime('%d/%m/%Y')
    print(nascimeto_str)
    confirmacao = int(input('A data que você informou esta correta?\nDigite 1 se SIM ou 2 se NÃO: ' ))

    while confirmacao == 2:
        print('Digite novamente!')
        ano = int(input('Qual o ano que você nasceu: '))
        mes = int(input('Qual o mes que você nasceu: '))
        dia = int(input('Qual o dia que você nasceu: '))
        nascimeto = date(ano, mes, dia)
        print(nascimeto)
        confirmacao = int(input('A data que você informou esta correta?\nDigite 1 se SIM ou 2 se NÃO: '))

    idade = hoje - nascimeto
    idade_str = idade.days
    print('Fazem {} dias desde a data que você colocou!'.format(idade_str))

if __name__ == '__main__':
    calculadora_dias()