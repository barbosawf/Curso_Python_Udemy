"""
Min e Max

max() → retorna o maior valor de um iterável ou o maior de dois, ou mais elementos
"""
# Exemplo 01
print('Exemplo 01:')
lista = [1, 8, 4, 99, 34, 129]

print('lista:      ', lista)
print('max(lista): ', max(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print('\ndicionario:               ', dicionario)
print('max(dicionario):          ', max(dicionario))
print('max(dicionario.values()): ', max(dicionario.values()))

# Exemplo 02. Os elementos podem ser passados diretamente na função.
print('\nExemplo 02. Os elementos podem ser passados diretamente na função:')

print('max(5, 7):                    ', max(5, 7))
print('max(2, 7, 11, 3):             ', max(2, 7, 11, 3))
print("max('b', 'g', 'i', 'c'):      ", max('b', 'g', 'i', 'c'))


# Exemplo 03. Programa que recebe valores e retorna o maior.
print('\nExemplo 03. Programa que recebe valores e retorna o maior.')

# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))

# print(f'O maior valor digitado é {max(val1, val2)}')

# Exemplo 04. Em lista de ‘strings’, max e min consideram a ordem alfabética.
print('\nExemplo 04. Em lista de strings, max e min levam em consideração a ordem alfabética.\n')

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivier', 'Ivan']

print('nomes: ', nomes)
print('max(nomes): ', max(nomes))
print('min(nomes): ', min(nomes))

# Exemplo 05. Utilizando o key da função
print('\nExemplo 05. Utilizando o key da função.\n')

print('nomes: ', nomes)
print('max(nomes, key=lambda nome: len(nome)): ', max(nomes, key=lambda nome: len(nome)))
print('min(nomes, key=lambda nome: len(nome)): ', min(nomes, key=lambda nome: len(nome)))

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

print("max(musicas, key=lambda musica: musica['tocou']): ")
print(max(musicas, key=lambda musica: musica['tocou']))

print("\nmin(musicas, key=lambda musica: musica['tocou']): ")
print(min(musicas, key=lambda musica: musica['tocou']))

print("\nmin(musicas, key=lambda musica: musica['tocou'])['titulo']: ")
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Exemplo 07
print('\nExemplo 07')

for c, dicionario in enumerate(musicas):
    if c == 0:
        n_mais_tocada = dicionario['tocou']
    if dicionario['tocou'] > n_mais_tocada:
        music_mais_tocada = dicionario['titulo']


print("""
for c, dicionario in enumerate(musicas):
    if c == 0:
        n_mais_tocada = dicionario['tocou']
    if dicionario['tocou'] > n_mais_tocada:
        music_mais_tocada = dicionario['titulo']
        """)

print('music_mais_tocada: ', music_mais_tocada)
