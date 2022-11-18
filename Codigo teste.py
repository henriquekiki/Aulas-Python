#Código criado por mim, utilizando alguns métodos que aprendi durante o curso.
# É simples e inconclusivo, mas serve pra adicionar um animal na lista e se o animal ja estiver na lista, não é adicionado.
# Sei que ainda falta muita coisa pra esse codigo ficar bom, mas vou atualizando ele durante o curso.

novo_animal = input('Digite o animal que deseja colocar na lista: ')

lista_animal = ['Cachorro', 'Gato', 'Elefante', ]

if novo_animal in lista_animal:
    print('Este animal já esta na lista!\n{}'.format(lista_animal))
else:
    print('Animal adicionado.')
    lista_animal.append(novo_animal)
    print(lista_animal)

