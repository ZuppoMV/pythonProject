contador = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador(lista_animais))

soma = lambda a,b: a + b
print(soma(5,10))


calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}
print(type(calculadora))

soma = calculadora['soma']
multipl = calculadora['mult']
print(soma(10, 5))
print(multipl(30,2))

