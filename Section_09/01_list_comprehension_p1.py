"""
List Comprehension

- Pode-se gerar novas listas om dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]
"""
from typing import List

# Exemplo 01
print('Exemplo 01')

numeros = [1, 2, 3, 4, 5]

res1 = [num * 10 for num in numeros]
res2 = [num / 2 for num in numeros]


print("""
numeros = [1, 2, 3, 4, 5]

res1 = [num * 10 for num in numeros]
res2 = [num / 2 for num in numeros]
""")

print('res1: ', res1)
print('res2: ', res2)

# Exemplo 02
print('\nExemplo 02')

numeros = [1, 2, 3, 4, 5]


def funcao(valor):
    return valor * valor


res = [funcao(num) for num in numeros]

print("""
numeros = [1, 2, 3, 4, 5]


def funcao(valor):
    return valor * valor


res = [funcao(num) for num in numeros]
""")

print('res: ', res)


# List Comprehension versus Loop
print('\nList Comprehension versus Loop')
print('\nLoop')

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for num in numeros:
    num_dobrado = num * 2
    numeros_dobrados.append(num_dobrado)

print("""
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for num in numeros:
    num_dobrado = num * 2
    numeros_dobrados.append(num_dobrado)
    """)

print('numeros_dobrados: ', numeros_dobrados)

print('\nList Comprehension')
print('[num * 2 for num in numeros]):         ', [num * 2 for num in numeros])
print('[num * 2 for num in [1, 2, 3, 4, 5]]): ', [num * 2 for num in [1, 2, 3, 4, 5]])

# Outros Exemplos
print('\nOutros Exemplos: ')

# Exemplo 01
print('\nExemplo 01: ')

nome = 'Geek University'
print('nome:                              ', nome)
print('[letra.upper() for letra in nome]: ', [letra.upper() for letra in nome])

# Exemplo 02
print('\nExemplo 02: ')

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


print('amigos: ', amigos)
print("""
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
    """)

print('[amigo[0].upper() for amigo in amigos]:  ', [amigo[0].upper() for amigo in amigos])
print('[amigo.title() for amigo in amigos]:     ', [amigo.title() for amigo in amigos])
print('[caixa_alta(amigo) for amigo in amigos]: ', [caixa_alta(amigo) for amigo in amigos])


# Exemplo 03
print('\nExemplo 03: ')

print('[num * 3 for num in range(1, 10)]: ', [num * 3 for num in range(1, 10)])

# Exemplo 04
print('\nExemplo 04: ')

print('[bool(valor) for valor in [0, [], '', True, 1, 3.14]]: ', [bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 05
print('\nExemplo 05: ')

print('[str(num) for num in [1, 2, 3, 4, 5]]: ', [str(num) for num in [1, 2, 3, 4, 5]])
