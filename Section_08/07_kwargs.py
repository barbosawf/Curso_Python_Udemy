"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chmamos de **kwargs

kwargs exige que os parâmetros sejam nomeados e transforma esses parâmetros extras em dicionários
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo 01
print(f'{a}Exemplo 01{c}')


def cores_favoritas(**kwargs):
    return kwargs


print(f"""{b}
def cores_favoritas(**kwargs):
    return kwargs{c}
""")

print("cores_favoritas(marcos='verde', julia='amarelo', rafael='azul'): ",
      cores_favoritas(marcos='verde', julia='amarelo', rafael='azul'))

# Exemplo 02
print(f'{a}\nExemplo 02{c}')


def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f'A cor favorida de {nome.title()} é {cor}!')


print(f"""{b}
def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print f'A cor favorida de {{nome}} é {{cor}}!'{c}
        """)

print("cores_favoritas(marcos='verde', julia='amarelo', rafael='azul')")
cores_favoritas(marcos='verde', julia='amarelo', rafael='azul')

# Exemplo mais complexo
print(f'{a}\nExemplo 03: mais complexo{c}')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(f"""{b}
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico!'
    elif 'geek' in kwargs:
        return f"{{kwargs['geek']}} Geek!"
    return 'Não tenho certeza quem você é...'{c}
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


print(f"""{b}
As funções podem ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros (não obrigatórios);
- **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{{nome}} tem {{idade}} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Não solteiro')
    print(kwargs, '\n'){c}
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
print(f'\n{a}Entendendo a ordem dos parâmetros numa função (ordem CORRETA):{c}')


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(f"""{b}
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]{c}
""")

print("mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor')): ")
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Entendendo a ordem dos parâmetros numa função (ordem INCORRETA):
print(f'\n{a}Entendendo a ordem dos parâmetros numa função (ordem INCORRETA):{c}')


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(f"""{b}
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]{c}
""")

print("mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor')): ")
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

print('A tupla do args ficou vazia e o instrutor recebeu 3. Por isso, deve-se colocar a ordem correta.')


# Desempacotar com **kwargs:
print(f'{a}\n# Desempacotar com **kwargs:{c}')


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones', 'idade': 8}


print(f"""{b}
def mostra_nomes(**kwargs):
    return f"{{kwargs['nome']}} {{kwargs['sobrenome']}}"


nomes = {{'nome': 'Felicity', 'sobrenome': 'Jones', 'idade': 8}}{c}
""")

print('mostra_nomes(**nomes): ', mostra_nomes(**nomes))

# Outro exemplo de desempacotamento de dicionário:
print(f'\n{a}Outro exemplo de desempacotamento de dicionário:{c}')

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)


def soma_tres_numeros(a, b, c):
    return a + b + c


print(f"""{b}
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {{1, 2, 3}}
dicionario = dict(a=1, b=2, c=3)


def soma_tres_numeros(a, b, c):
    return a + b + c{c}
    
    """)

print('soma_tres_numeros(*lista): ', soma_tres_numeros(*lista))
print('soma_tres_numeros(*tupla): ', soma_tres_numeros(*tupla))
print('soma_tres_numeros(*conjunto): ', soma_tres_numeros(*conjunto))
print('soma_tres_numeros(**dicionario): ', soma_tres_numeros(**dicionario))

# Os nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função:
print(f'\n{a}Os nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função:{c}')

print(f"""{b}
def soma_tres_numeros(a, b, c):
    return a + b + c


dicionario = dict(d=1, e=2, f=3)

try:
    print(soma_tres_numeros(**dicionario))
except TypeError:
    print('Os nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função.')
{c}
""")


def soma_tres_numeros(a, b, c):
    return a + b + c


dicionario = dict(d=1, e=2, f=3)


try:
    print(soma_tres_numeros(**dicionario))
except TypeError:
    print('Os nomes das chaves num dicionário devem ser os mesmos dos parâmetros da função.')
