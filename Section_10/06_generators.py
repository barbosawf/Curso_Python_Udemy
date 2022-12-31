"""
Generators = Tuple Comprehension
"""

# Exemplo 01. Usa parênteses, mas não retorna tupla e sim um generator object:
print('Exemplo 01. Usa parênteses, mas não retorna tupla e sim um generator object:\n')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print('nomes:                                   ', nomes)
print("(nome[0] == 'C' for nome in nomes):      ", (nome[0] == 'C' for nome in nomes))
print("tuple(nome[0] == 'C' for nome in nomes): ", tuple(nome[0] == 'C' for nome in nomes))


# Exemplo 02. Usa parênteses, mas não retorna tupla e sim um generator object:
print('\n# Exemplo 02. Usa parênteses, mas não retorna tupla e sim um generator object:\n')

res = (nome[0] == 'C' for nome in nomes)
print("res = (nome[0] == 'C' for nome in nomes)")
print('type(res): ', type(res))
print('tuple(res): ', tuple(res))
print('tuple(res): ', tuple(res), "Fica vazio, pois a partir do seu uso pela primeira vez ele é exluído da memória.")
print('Obs.: Generator ocupa menos recurso na memória em relação as listas, conjuntos e dicionários comprehension.')

# Exemplo 03. getsizeof da biblioteca sys mostra quantos bytes um objeto ocupa na memória.
print('\n# Exemplo 03. getsizeof da biblioteca sys mostra quantos bytes um objeto ocupa na memória.')

from sys import getsizeof

print("getsizeof(3):            ", getsizeof(3))
print("getsizeof(45):           ", getsizeof(45))
print("getsizeof(4439875295):   ", getsizeof(4439875295))
print("getsizeof('Geek'):       ", getsizeof('Geek'))
print("getsizeof('University'): ", getsizeof('University'))
print("getsizeof(nomes):        ", getsizeof(nomes))

# Exemplo 04. getsizeof da biblioteca sys mostra quantos bytes um objeto ocupa na memória.
print('\n# Exemplo 04. getsizeof da biblioteca sys mostra quantos bytes um objeto ocupa na memória.')

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
generator = getsizeof((x * 10 for x in range(1000)))

print("""
list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
generator = getsizeof((x * 10 for x in range(1000)))

""")

print('list_comp: ', list_comp)
print('set_comp:  ', set_comp)
print('dict_comp: ', dict_comp)
print('generator: ', generator)

# Exemplo 05. Iterar com Generator Expression:
print('\nExemplo 05. Iterar com Generator Expression:')

gen = (x * 10 for x in range(10))
print('gen: ', gen)


print("""
for num in gen:
    print(num, end=' ')
print(' ')
""")

for num in gen:
    print(num, end=' ')
print(' ')
