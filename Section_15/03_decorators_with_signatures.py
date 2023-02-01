"""
Decoradores com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto chamado de Decorator Pattern
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Relebrando decorators
print(f'{a}Relebrando decorators{c}')

print(f"""{b}
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {{nome}}!'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {{principal}}, acompanhado de {{acompanhamento}}, por favor!'
    
print(saudacao('Wagner'))

try:
    print(ordenar('Arroz', 'Feijão'))
except TypeError as er:
    print(f'Dá errado por precisa de dois parâmetros e só recebe um: {{er}}')
{c}""")


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}!'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


print(saudacao('Wagner'),'\n')

try:
    print(ordenar('Arroz', 'Feijão'))
except TypeError as er:
    print(f'Dá errado por precisa de dois parâmetros e só recebe um: {er}')


# Refatorando para dar certo
print(f'\n{a}Refatorando para dar certo{c}')

print(f"""{b}
def gritar(funcao):  # o nome da função e os parâmetros dela são assinaturas da função
    def aumentar(*args):
        return funcao(*args).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {{nome}}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {{principal}} acompanhado de {{acompanhamento}}.'


print(saudacao('Felicity'))
print(ordenar('Picanha', 'Batata Frita')){c}
""")


def gritar(funcao):  # o nome da função e os parâmetros dela são assinaturas da função
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}.'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}.'


print("saudacao('Felicity'): ", saudacao('Felicity'))
print("\nordenar('Picanha', 'Batata Frita'): ", ordenar('Picanha', 'Batata Frita'))
print("\nordenar(acompanhamento='Batata Frita', principal='Picanha'): ",
      ordenar(acompanhamento='Batata Frita', principal='Picanha'))


# Decorators com parâmetros de entrada
print(f'\n{a}Decorators com parâmetros de entrada{c}')


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorretor! Primeiro argumento precisa ser {valor}!'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(f"""{b}
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorretor! Primeiro argumento precisa ser {{valor}}!'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2{c}
""")

print("\nprint(comida_favorita('pizza', 'lasanha', 'picanha', 'costelinha suína ao molho barbecue')): ")
print(comida_favorita('pizza', 'lasanha', 'picanha', 'costelinha suína ao molho barbecue'))

print("\nprint(comida_favorita('lasanha', 'picanha', 'costelinha suína ao molho barbecue', 'pizza')): ")
print(comida_favorita('lasanha', 'picanha', 'costelinha suína ao molho barbecue', 'pizza'))

print("\nprint(soma_dez(10, 12)): ")
print(soma_dez(10, 12))

print("\nprint(soma_dez(1, 21)): ")
print(soma_dez(1, 21))