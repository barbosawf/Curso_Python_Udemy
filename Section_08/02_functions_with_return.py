"""
OBS.: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

A palavra return é que faz a função retornar o valor
"""

# Função sem retorno
print('Função sem retorno')


def quadrado_de_7():
    print(7 * 7)


print("\n"
      "def quadrado_de_7():\n"
      "    print(7 * 7)\n")


ret = quadrado_de_7()

print('\nret = quadrado_de_7()')
print('quadrado_de_7():', quadrado_de_7())
print('ret: ', ret)

# Função com retorno
print('\nFunção com retorno')


def quadrado_de_7():
    return 7 * 7


print("""
def quadrado_de_7():
    return 7 * 7
""")

ret = quadrado_de_7()
print('ret = quadrado_de_7()')
print('quadrado_de_7():', quadrado_de_7())
print('ret: ', ret)
print('quadrado_de_7() + 1:', quadrado_de_7() + 1)

"""
OBS.: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter fiferentes returns em uma função;
3 - Podemos retornar qualquer tipo de dado e até mesmo múltiplos valores em uma função.
"""

# Exemplo 01
print('\nExemplo 01')


def diz_oi():
    print('Estou sendo executado antes do return!')
    return 'Oi!'
    print('Estou sendo executado após o return!')


print(diz_oi())


# Exemplo 02
print('\nExemplo 02')


def nova_funcao1():
    var = True
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'


def nova_funcao2():
    var = None
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'


def nova_funcao3():
    var = False
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'


print("""
def nova_funcao1():
    var = True
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'


def nova_funcao2():
    var = None
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'
    

def nova_funcao3():
    var = False
    if var:
        return 4
    elif var is None:
        return 5.5
    else:
        return 'b'
""")

print('nova_funcao1(): ', nova_funcao1())
print('nova_funcao2(): ', nova_funcao2())
print('nova_funcao3(): ', nova_funcao3())

# Exemplo 03
print('\nExemplo 03')


def outra_funcao():
    return 1, 2, 3, 4, 5


num = outra_funcao()

num1, num2, num3, num4, num5 = outra_funcao()

print("""
def outra_funcao():
    return 1, 2, 3, 4, 5

num = outra_funcao()

num1, num2, num3, num4, num5 = outra_funcao()
""")

print('num: ', num)
print('num1: ', num1)
print('num2: ', num2)
print('num3: ', num3)
print('num4: ', num4)
print('num5: ', num5)

# Exemplo 03
print('\nExemplo 03')

from random import random


def joga_moeda():
    # Gera um número aleatório entre 0 e 1:
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print("""
from random import random


def joga_moeda():
    # Gera um número aleatório entre 0 e 1:
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'
""")

print('joga_moeda(): ', joga_moeda())

