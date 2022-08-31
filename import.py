from televisao import Televisao
from contador import contador_letras, teste
from calc1 import Calculadora


televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora (5,10)
print(calculadora.soma())
lista = [ 'formiga', 'barata', 'rato',]
total_letras = contador_letras(lista)
print('Total de letras: {}'.format(total_letras))
print(teste())
