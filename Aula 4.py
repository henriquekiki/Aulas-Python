a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou a nota errada! \nPrimeiro bimestre: '))

b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou a nota errada! \nSegundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou a nota errada! \nTerceiro bimestre: '))

d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou a nota errada! \nQuarto bimestre: '))
media = (a + b + c + d) / 4
if media >= 5:
    print('APROVADO!')
else:
    print('REPROVADO!')

print(int(media))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1



#Daqui pra baixo, codigo pra encontrar número primo de 0 ate o valor digitado.

# a = int(input('Entre com valor: '))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#        # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

#______________________________________________________________________________________________________________________



# a = int(input('Entre com o numero: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))



