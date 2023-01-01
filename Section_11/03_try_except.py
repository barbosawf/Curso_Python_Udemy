"""
O bloco try/except

Serve para tratar erros que possam ocorrer no código.
Precine que o programa pare de funcionar e o utilizador receba mensagens de erro inesperadas.

Como usar:
try:
    //execução problemática.
except:
    //o que deve ser feito em caso de problema.

OBS. Tratar erros de forma genérica não é a melhor forma de fazer. O ideal é sempre tratar especificamente.
"""

# Exemplo 01. Tratamento de um erro genérico.
print('Exemplo 01. Tratamento de um erro genérico.')


print("""
try:
    geek()  # dá erro porque a função não foi definida.
except:
    print('Deu algum problema.')
""")

try:
    geek()  # dá erro porque a função não foi definida.
except:
    print('Deu algum problema.')

# Exemplo 02. Tratamento de um erro genérico.
print('\nExemplo 02. Tratamento de um erro genérico.')


print("""
try:
    len(5)  # dá erro porque a função não foi definida.
except:
    print('Deu algum problema.')
""")

try:
    len(5)  # dá TypeError porque 5 não é um iterável.
except:
    print('Deu algum problema.')

# Exemplo 03. Tratamento de um erro específico.
print('\nExemplo 03. Tratamento de um erro específico.')

print("""
try:
    geek()  # dá erro porque a função não foi definida.
except NameError:
    print('Você está utilizando uma função inexistente.')
    """)

try:
    geek()  # dá erro porque a função não foi definida.
except NameError:
    print('Você está utilizando uma função inexistente.')


# Exemplo 04. Tratamento de um erro específico.
print('\nExemplo 04. Tratamento de um erro específico.')

print("""
try:
    len(5)  # TypeError porque 5 não é um iterável.
except TypeError:  # Tem que saber qual é o erro para colocar aqui.
    print('Você colocou um não-iterável na função.')
    """)

try:
    len(5)  # TypeError porque 5 não é um iterável.
except TypeError:  # Tem que saber qual é o erro para colocar aqui.
    print('Você colocou um não-iterável na função.')

# Exemplo 05. Tratamento de um erro específico.
print('\nExemplo 05. Tratamento de um erro específico.')

print("""
try:
    len(5)  # TypeError porque 5 não é um iterável.
except TypeError:  # Tem que saber qual é o erro para colocar aqui.
    print('Você colocou um não-iterável na função.')
    """)

try:
    len(5)  # TypeError porque 5 não é um iterável.
except TypeError as err:  # Tem que saber qual é o erro para colocar aqui.
    print(f'A aplicaçao gerou o seguinte erro: {err}.')


# Exemplo 06. Pode-se efetuar diversos tratametos de erro de uma vez.
print('\nExemplo 06. Pode-se efetuar diversos tratametos de erro de uma vez.')

from random import sample

x = sample(range(3), 1)[0]

print("""
try:
    if x == 0:
        len(5)  # TypeError porque 5 não é um iterável.
    elif x == 1:
        geek()
    else:
        'Geek'[9]  # IndexError, mas será tratado como erro genérico.
except TypeError as erra:
    print(f'Ocorreu um TypeError: {erra}.')
except NameError as errb:
    print(f'Ocorreu um NameError: {errb}.')
except:
    print('Deu um erro genérico não identificado.')
    """)

try:
    if x == 0:
        len(5)  # TypeError porque 5 não é um iterável.
    elif x == 1:
        geek()
    else:
        'Geek'[9]  # IndexError, mas será tratado como erro genérico.
except TypeError as erra:
    print(f'Ocorreu um TypeError: {erra}.')
except NameError as errb:
    print(f'Ocorreu um NameError: {errb}.')
except:
    print('Deu um erro genérico não identificado.')


# Exemplo 07.
print('\nExemplo 07.')


def pega_valor(dicionário, chave):
    try:
        return dicionário[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

print("""
def pega_valor(dicionário, chave):
    try:
        return dicionário[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}
""")

print("pega_valor(dic, 'nome'): ", pega_valor(dic, 'nome'))
print("pega_valor(dic, 'game'): ", pega_valor(dic, 'game'))
print("pega_valor(7, 'nome'):   ", pega_valor(7, 'nome'))


