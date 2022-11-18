a = int(input('Digite a primeira nota: '))
while a > 10:
    a = int(input('Nota errada! Digite novamente.\nDigite a primeira nota: '))

#================================================
b = int(input('Digite a segunda nota: '))
while b > 10:
    b = int(input('Nota errada! Digite novamente.\nDigite a segunda nota: '))

#================================================
c = int(input('Digite a terceira nota: '))
while c > 10:
    c = int(input('Nota errada! Digite novamente.\nDigite a terceira nota: '))

#================================================
d = int(input('Digite a quarta nota: '))
while d > 10:
    d = int(input('Nota errada! Digite novamente.\nDigite a quarta nota: '))

#================================================

media = (a + b + c + d) / 4

if media >= 5:
    print('APROVADO!')
    print("Média: {}".format(int(media)))
else:
    print('REPROVADO!')
    print('Média: {}'.format(int(media)))