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

print('amigos: ', amigos)
print('[amigo[0].upper() for amigo in amigos]: ', [amigo[0].upper() for amigo in amigos])
print('[amigo.title() for amigo in amigos]: ', [amigo.title() for amigo in amigos])
