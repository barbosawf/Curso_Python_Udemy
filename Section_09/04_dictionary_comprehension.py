"""
Dictionary Comprehension

Síntaxy
{chave: valor for valor in iterável}
"""

# Exemplo 01
print('Exemplo 01')

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print("""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
Para cada chave, valor dentro do iterável, adicione chave e coloque o valor ao quadrado
""")

print('numeros:         ', numeros)
print('numeros.items(): ', numeros.items())
print('quadrado:        ', quadrado)

# Exemplo 02
print('\nExemplo 02')

numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}

print("""
numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}
""")

print('numeros:   ', numeros)
print('quadrado:  ', quadrado)


# Exemplo 03. Dicionário não tem repetição de chave. Então cuidado!
print('\nExemplo 03. Dicionário não tem repetição de chave. Então cuidado!')

numeros = [1, 2, 3, 4, 5, 1, 4, 3, 2]
quadrado = {valor: valor ** 2 for valor in numeros}

print("""
numeros = [1, 2, 3, 4, 5, 1, 4, 3, 2]
quadrado = {valor: valor ** 2 for valor in numeros}
""")

print('numeros:   ', numeros)
print('quadrado:  ', quadrado)

# Exemplo 04
print('\nExemplo 04')

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print("""
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
""")

print('mistura: ', mistura)

# Exemplo 05 (com lógica condicional)
print('\nExemplo 04 (com lógica condicional)')

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if not num % 2 else 'impar') for num in numeros}

print("""
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if not num % 2 else 'impar') for num in numeros}
""")

print('res: ', res)


