# Codigo criado por mim. Vou aperfeiçoando ele no decorrer do curso.
# Pretendo fazer uma lista pra incluir nomes de animais.
# Consegui fazer a lista. Mas ela ainda adiciona o mesmo animal caso escreva alguma letra maiuscula ou minuscula
# diferente no nome do animal.
lista_animal = []
a = input('Digite um animal: ')
if a in lista_animal:
    print('Animal já está na lista.')
else:
    lista_animal.append(a)
    print('Animal adicionado.\n', lista_animal)
while a:
    a = input('Digite um animal: ')
    if a in lista_animal:
        print('Animal já está na lista.')
    else:
        lista_animal.append(a)
        print('Animal adicionado.\n', lista_animal)
