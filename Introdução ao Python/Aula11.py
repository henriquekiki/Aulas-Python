
# lista = [1, 10]
# try:
#     divisao = 10 / 1
#     numero = lista[1]
#
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0.')
# except IndexError:
#     print('Erro ao acessar um indece inválido da lista.')
# except BaseException as ex:
#     print('Erro desconhecido.\nErro: {}'.format(ex))
#------------------------------------------------------------------

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma notade 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        break
    except ValueError:
        print('Valor inválido.\nDeve-se digitar apenas números.')
    except InputError as ex:
        print(ex)