"""
Sorted

Não é o sort(), pois funciona só para listas.

Pode-se utilizar o sorted() com qualquer iterável.

O sorted() serve para ordenar.
"""

# Exemplo 01 (com lista)
print('Exemplo 01 (com lista)')

numeros = [2, 5, 3, 1, 4]
print('numeros: ', numeros)
print('sorted(numeros): ', sorted(numeros))
print('numeros: ', numeros, 'O sorted() não muda a lista original, pois retorna uma nova lista.')

# Exemplo 02 (com tupla)
print('\nExemplo 02 (com tupla)')

numeros = (2, 5, 3, 1, 4)
print('numeros: ', numeros)
print('sorted(numeros): ', sorted(numeros), 'Retorna sempre uma lista.')
print('numeros: ', numeros, 'O sorted() não muda a tupla original, pois retorna uma nova lista.')


# Exemplo 03 (com set)
print('\nExemplo 02 (com set)')

numeros = {2, 5, 3, 1, 4}
print('numeros: ', numeros)
print('sorted(numeros): ', sorted(numeros), 'Retorna sempre uma lista.')
print('numeros: ', numeros, 'O sorted() não muda tipo de objeto, mas retorna sempre uma nova lista.')

# Exemplo 04 (com lista e adicionando argumentos na função)
print('\nExemplo 04 (com lista e adicionando argumentos na função)')

numeros = [2, 5, 3, 1, 4]
print('numeros: ', numeros)
print('sorted(numeros, reverse=True): ', sorted(numeros, reverse=True))
print('Ordena inversamente.')

# Exemplo 05
print('\nExemplo 05')

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Terminei de escovar os dentes', 'Viajar é bom d+']},
    {'username': 'gal', 'tweets': []},
    {'username': 'lisandra', 'tweets': ['Vou sair hoje', 'Acabei não saindo']},
]

print("""
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Terminei de escovar os dentes']},
    {'username': 'gal', 'tweets': []},
    {'username': 'lisandra', 'tweets': ['Vou sair hoje', 'Acabei não saindo']},
]
""")

print("sorted(usuarios, key=lambda usuario: usuario['username']): ")
print(sorted(usuarios, key=lambda usuario: usuario['username']))

print("\nsorted(usuarios, key=lambda usuario: usuario['username'], reverse=True): ")
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

print("\nsorted(usuarios, key=lambda usuario: len(usuario['tweets']))")
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


# Exemplo 06
print('\nExemplo 06')

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 32},
    {'titulo': "Too old to rock'in'roll", 'tocou': 16},
    {'titulo': 'Read sea', 'tocou': 7},
    {'titulo': 'War of Gods', 'tocou': 77}
]

print("""
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 32},
    {'titulo': "Too old to rock'in'roll", 'tocou': 16},
    {'titulo': 'Read sea', 'tocou': 7},
    {'titulo': 'War of Gods', 'tocou': 77}
]
""")

print("sorted(musicas, key=lambda musica: musica['tocou']): ")
print(sorted(musicas, key=lambda musica: musica['tocou']))

print("sorted(musicas, key=lambda musica: musica['tocou'], reverse=True): ")
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
