from Aula6_TV import Televisao
from Aula6_calculadora import Calculadora
from Aula8_importação import contador_letras


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(10, 2)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
