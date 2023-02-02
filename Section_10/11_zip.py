"""
zip() -> cria um iterável que agrega elemento de cada um dos iteráveis passados como entrada em pares.
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo 01
print(f'{a}Exemplo 01{c}')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print('lista1: ', lista1)
print('lista2: ', lista2)

zip1 = zip(lista1, lista2, 'ABC')
zip2 = zip(lista1, lista2)
zip3 = zip(lista1, lista2)
zip4 = zip(lista1, lista2)

print(f"""{b}
zip1 = zip(lista1, lista2, 'ABC')
zip2 = zip(lista1, lista2)
zip3 = zip(lista1, lista2)
zip4 = zip(lista1, lista2){c}
""")

print('zip1:       ', zip1)
print('type(zip1): ', type(zip1))

print('\nlist(zip1):  ', list(zip1))
print('set(zip2):   ', set(zip2))
print('\ntuple(zip3): ', tuple(zip3))
print('tuple(zip3): ', tuple(zip3), 'Pode ser usado apenas uma vez.')
print('\ndict(zip4): ', dict(zip4), 'Neste caso, pode-se apenas duas listas: uma para chave outra para valor.')

# Exemplo 02. Elementos a mais em qualquer lista é desconsiderado.
print(f'\n{a}Exemplo 02. Elementos a mais em qualquer lista é desconsiderado.{c}')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = ['A', 'B', 'C', 'D', 'E']

print(f"""{b}
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = ['A', 'B', 'C', 'D', 'E']{c}
""")

zip1 = zip(lista1, lista2, lista3)

print("zip1 = zip(lista1, lista2, lista3): ")
print('list(zip1): ', list(zip1))

zip1 = zip(lista3, lista1, lista2)

print("\nzip1 = zip(lista3, lista1, lista2): ")
print('list(zip1): ', list(zip1))

# Exemplo 03. Pode-se utilizar diferentes iteráveis com zip.
print(f'\n{a}Exemplo 03. Pode-se utilizar diferentes iteráveis com zip.{c}')

tupla = 1, 2, 3, 4, 5
lista = ['A', 'C', 'C', 'B']
dicionario = {'a': 4, 2: 5, 3: 6}

print(f"""{b}
tupla = 1, 2, 3, 4, 5
lista = ['A', 'C', 'C', 'B']
dicionario = {{'a': 4, 2: 5, 3: 6}}{c}
""")

zip1 = zip(tupla, lista, dicionario)
print('zip1 = zip(tupla, lista, dicionario): ')
print('list(zip1): ', list(zip1))

zip1 = zip(tupla, lista, dicionario.values())
print('\nzip1 = zip(tupla, lista, dicionario.values()): ')
print('list(zip1): ', list(zip1))

# Exemplo 04. Lista de tuplas com desempacotamento.
print(f'\n{a}Exemplo 04. Lista de tuplas com desempacotamento.{c}')

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(f'\n{b}dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]{c}')

print('\nlist(zip(*dados)): ', list(zip(*dados)))

# Exemplo 05.
print(f'\n{a}Exemplo 05.{c}')

alunos = ['maria', 'josé', 'abraão']
prova1 = [80, 91, 78]
prova2 = [98, 89, 67]

print(f"""{b}
alunos = ['maria', 'josé', 'abraão']
prova1 = [80, 91, 78]
prova2 = [98, 89, 67]{c}
""")


print('list(zip(alunos, prova1, prova2)): ', list(zip(alunos, prova1, prova2)))
final = {tupla[0]: max(tupla[1], tupla[2]) for tupla in zip(alunos, prova1, prova2)}
print("\nfinal = {tupla[0]: max(tupla[1], tupla[2]) for tupla in zip(alunos, prova1, prova2)}")

print('final: ', final)

# Exemplo 06.
print(f'\n{a}Exemplo 06.{c}')

alunos = ['maria', 'josé', 'abraão']
prova1 = [80, 91, 78]
prova2 = [98, 89, 67]

print(f"""{b}
alunos = ['maria', 'josé', 'abraão']
prova1 = [80, 91, 78]
prova2 = [98, 89, 67]{c}
""")


print('list(zip(alunos, prova1, prova2)): ', list(zip(alunos, prova1, prova2)))
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print("\nfinal = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))")

print('dict(final): ', dict(final))
