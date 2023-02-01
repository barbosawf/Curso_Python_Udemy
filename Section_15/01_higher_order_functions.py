"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?
-  Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
   que retornam outras funções como resultado ou mesmo que podemos passar funções
   como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
   nos nossos programas.


Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizens
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo - Definindo as funções
print(f'\n{a}# Exemplo - Definindo as funções{c}')


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(f"""{b}
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2){c}
""")

print(f"""
calcular(10, 2, somar):       {calcular(10, 2, somar)}
calcular(10, 2, diminuir):    {calcular(10, 2, diminuir)}
calcular(10, 2, multiplicar): {calcular(10, 2, multiplicar)}
calcular(10, 2, dividir):     {calcular(10, 2, dividir)}
""")

# Nested functions
print(f'\n{a}Nested functions{c}')

"""
Em Python, podemos ter funções dentro de funções, que são conhecidas por Nested Funcions
ou também, Inner Functions"""

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí, ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessoa + '!'


print(f"""{b}
def cumprimento(pessoa):
    def humor():
        return choice(('E aí, ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessoa + '!'{c}
""")

print("cumprimento('Felicity'): ", cumprimento('Felitity'))


# Retornando funções de outras funções
print(f'\n{a}Retornando funções de outras funções{c}')


def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkkkk', 'yayayaya'))
    return rir  # aqui está retornando a função e não sua execução


rindo = faz_me_rir()

print(f"""{b}
def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkkkk', 'yayayaya'))
    return rir  # aqui está retornando a função e não sua execução


rindo = faz_me_rir(){c}
""")

print('rindo(): ', rindo())

# Inner Functions (Funções Internas/Nested Functions) podem acessar o escopo de funções mais externas.

print(f'\n{a}Inner Functions (Funções Internas/Nested Functions) podem acessar o escopo de funções mais externas.{c}')


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'kkkkkkk', 'yayayaya'))
        return f'{risada}, {pessoa}!'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')

print(f"""{b}
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'kkkkkkk', 'yayayaya'))
        return f'{{risada}}, {{pessoa}}!'
    return dando_risada
    
rindo = faz_me_rir_novamente('Fernanda'){c}
""")

print('rindo(): ', rindo())
print('rindo(): ', rindo())
print('rindo(): ', rindo())


print()


