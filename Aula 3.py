# Daqui pra baixo, codigo pra calcular media e dizer se esta aprovado ou reprovado.

a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou a nota errada! \nPrimeiro bimestre: '))

b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou a nota errada! \nSegundo bimestre: '))

c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou a nota errada! \nTerceiro bimestre: '))

d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou a nota errada! \nQuarto bimestre: '))
media = (a + b + c + d) / 4
if media >= 5:
    print('APROVADO!')
else:
    print('REPROVADO!')

print(int(media))

#
# if soma < 11:
#     print(int(soma))
# if soma > 10:
#     print('10')

#________________________________________________________________________________________________________________________

# Daqui pra baixo, codigo pra saber numero par entre dois número

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b ==0:
#     print('Número par encontrado.')
#     if resto_a == 0:
#         print(int(a))
#     if resto_b == 0:
#         print(int(b))
# else:
#     print('Nenhum número par encontrado.')
# ________________________________________________________________________________________________________________________

# Daqui pra baixo, codigo pra saber se é par ou impar.

# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('O número é par.')
# else:
#     print('O número é impar.')
# ________________________________________________________________________________________________________________________

# Daqui pra baixo, codigo pra saber qual o maior numero.

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('O maior número é {}' .format(a))
# elif b > a and b > c:
#     print('O maior número é {}' .format(b))
# else:
#     print('O maior número é {}' .format(c))
# if a == b and a == c:
#     print('Os três são iguais.')
# print('FINAL DO PROGRAMA')

