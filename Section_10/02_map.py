"""
Map

Com map, fazemos mapeamento de valores para uma função.

map é uma função que recebe dois parâmetros, o primeiro uma  função e o segundo é um iterável.
map retorna um map object.
"""

import math


def area(r):
    """Calcula a área de um círculo com raio r"""
    return math.pi * (r ** 2)


print('''
def area(r):
    """Calcula a área de um círculo com raio r"""
    return math.pi * (r ** 2)
    ''')

print('area(2):   ', area(2))
print('area(5.3): ', area(5.3))

# Exemplo 01. Através de comprehensive list.
print('\nExemplo 01. Através de comprehensive list.')

raios = [2, 4, 7, 0.3, 10, 44]
calculos = [area(raio) for raio in raios]

print("""
raios = [2, 4, 7, 0.3, 10, 44]
calculos = [area(raio) for raio in raios]
""")

print('calculos: ', calculos)

# Exemplo 02. Através do map.
print('\nExemplo 02. Através do map.')

calculos = map(area, raios)
print('calculos = map(area, raios)')
print('calculos:        ', calculos)
print('type(calculos):  ', type(calculos))
print('list(calculos) : ', list(calculos))

# Exemplo 03. Através do map e utilizando uma expressão lambda.
print('\nExemplo 03. Através do map e utilizando uma expressão lambda')
areas = list(map(lambda r: math.pi * (r ** 2), raios))
print('areas = list(map(lambda r: math.pi * (r ** 2), raios)): ')
print('areas: ', areas)

# OBS. Depois da primeira utilização do resultado da função map(), ele zera. Vi apenas no console.
print('\nOBS. Depois da primeira utilização do resultado da função map(), ele zera. Vi apenas no console.')

# Exemplo 04. Conversão para Fareheint
print('\nExemplo 04.')

cidades = [('Berlim', 29), ('Cairo', 40), ('Rio de Janeiro', 33), ('Ipatinga', 36), ('Tókio', 27), ('Lobres', 22)]
print('cidades: ', cidades)

c_para_f = lambda dado: (dado[0], (9 / 5 * dado[1] + 32))  # tudo dentro de () retorna tupla. Se [] retorna lista.

print("\nc_para_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))")

print('list(map(c_para_f, cidades)): ', list(map(c_para_f, cidades)))

# Exemplo 05. Map com mais de um iterável.
print('\nExemplo 05. Map com mais de um iterável.')


def multiplica_ab(a, b):
    return a * b


def multiplica_abc(a, b, c):
    return a * b * c


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

print("""
def multiplica_ab(a, b):
    return a * b


def multiplica_abc(a, b, c):
    return a * b * c


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
""")
print('list(map(multiplica_ab, lista1, lista2)):          ', list(map(multiplica_ab, lista1, lista2)))
print('list(map(multiplica_abc, lista1, lista2, lista3)): ', list(map(multiplica_abc, lista1, lista2, lista3)))

# Exemplo 05. Map com mais de um iterável.
print('\nExemplo 05. Map com mais de um iterável.')


def soma(*args):
    return sum(args)


print("""
def soma(*args):
    return sum(args)
    """)

print('list(map(soma, lista1)):                 ', list(map(soma, lista1)))
print('list(map(soma, lista1, lista2)):         ', list(map(soma, lista1, lista2)))
print('list(map(soma, lista1, lista2, lista3)): ', list(map(soma, lista1, lista2, lista3)))
