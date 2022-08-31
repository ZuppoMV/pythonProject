class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao (self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == "__main__" :
    calculadora = Calculadora()
    print ( calculadora.soma(9,3))
    print ( calculadora.subtracao(8,5))
    print ( calculadora.multiplicacao(9,8))
    print ( calculadora.divisao(50,3))