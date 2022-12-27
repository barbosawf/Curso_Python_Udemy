"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chmamos de **kwargs

kwargs exige que os parâmetros sejam nomeados e transforma esses parâmetros extras em dicionários
"""

# Exemplo 01
print('Exemplo 01')


def cores_favoritas(**kwargs):
    return kwargs


print("cores_favoritas(marcos='verde', julia='amarelo', rafael='azul'): ",
      cores_favoritas(marcos='verde', julia='amarelo', rafael='azul'))

# Exemplo 02
print('\nExemplo 02')


def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f'A cor favorida de {nome.title()} é {cor}!')


print("""
def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print f'A cor favorida de {nome} é {cor}!'
        """)

print("cores_favoritas(marcos='verde', julia='amarelo', rafael='azul')")
cores_favoritas(marcos='verde', julia='amarelo', rafael='azul')

# Exemplo mais complexo
print('\n# Exemplo 03: mais complexo')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print("""
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'
    """)

print('cumprimento_especial(): ', cumprimento_especial())
print("cumprimento_especial(geek='Python'): ", cumprimento_especial(geek='Python'))
print("cumprimento_especial(geek='Oi'): ", cumprimento_especial(geek='Oi'))

"""
As funções podem ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros (não obrigatórios);
- **kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Não solteiro')
    print(kwargs, '\n')


print("""
As funções podem ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros (não obrigatórios);
- **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Não solteiro')
    print(kwargs, '\n')
    """)

print("minha_funcao(8, 'Júlia'): \n")
minha_funcao(44, 'Júlia')
minha_funcao(25, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(22, 'Lilian', solteiro=True)
minha_funcao(32, 'Jacob', 2, 3, 2, eu='Não', voce='Vai')
minha_funcao(33, 'Lorena', eu='tu', ele='nos', vos='eles')
minha_funcao(32, 'Jacob', 4, 4, 7, solteiro=True, eu='tinha', um='gato')
minha_funcao(32, 'Irineu', 9, 6, 7, eu='tinha', solteiro=True, um='gato')


# Entendendo a ordem dos parâmetros numa função (ordem CORRETA):
print('\nEntendendo a ordem dos parâmetros numa função (ordem CORRETA):')


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print("""
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]
""")
print("mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor')): ")
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Entendendo a ordem dos parâmetros numa função (ordem INCORRETA):
print('\nEntendendo a ordem dos parâmetros numa função (ordem INCORRETA):')


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print("""
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]
""")
print("mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor')): ")
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

print('A tupla do args ficou vazia e o instrutor recebeu 3. Por isso, deve-se colocar a ordem correta.')


# Desempacotar com **kwargs:
print('\n# Desempacotar com **kwargs:')


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones', 'idade': 8}


print("""
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones', 'idade': 8}
""")
print('mostra_nomes(**nomes): ', mostra_nomes(**nomes))

#
print('\nOutro exemplo de desempacotamento de dicionário:')

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)


def soma_tres_numeros(a, b, c):
    return a + b + c


print("""
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)


def soma_tres_numeros(a, b, c):
    return a + b + c
    
    """)
print('soma_tres_numeros(*lista): ', soma_tres_numeros(*lista))
print('soma_tres_numeros(*tupla): ', soma_tres_numeros(*tupla))
print('soma_tres_numeros(*conjunto): ', soma_tres_numeros(*conjunto))
print('soma_tres_numeros(**dicionario): ', soma_tres_numeros(**dicionario))

# Os nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função:
print('\nOs nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função:')

dicionario = dict(d=1, e=2, f=3)
print('soma_tres_numeros(**dicionario): ', soma_tres_numeros(**dicionario))
