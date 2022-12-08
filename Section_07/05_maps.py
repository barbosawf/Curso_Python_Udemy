"""
Mapas são conhecidos em Python como dicionários

Dicionários em Python são representados por chaves
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários:
print('Iterar sobre dicionários:')

print('receita: ', receita)

print("""
for chave in receita:
    print(chave)
""")
for chave in receita:
    print(chave)

print("""
for chave in receita:
    print(receita[chave])
""")
for chave in receita:
    print(receita[chave])

print("""
for chave in receita:
    print(f'{chave} = {receita[chave]}')
""")
for chave in receita:
    print(f'{chave} = {receita[chave]}')

print("""
for indice, chave in enumerate(receita):
    print(indice, chave)
""")
for indice, chave in enumerate(receita):
    print(indice, chave)

# Conhecer todas as chaves através do comando keys()
print('\n# Conhecer todas as chaves através do comando keys()')
print('receita.keys(): ', receita.keys())

print("""
for chave in receita.keys():
    print(receita[chave])
""")
for chave in receita.keys():
    print(receita[chave])

# Conhecer os valores através do comando values()
print('\nConhecer os valores através do comando values()')
print('receita.values(): ', receita.values())

print("""
for values in receita.values():
    print(values)
""")
for valor in receita.values():
    print(valor)

# Desempacotar dicionários:
print('\nDesempacotar dicionários:')

print('receita.items(): ', receita.items())
print("""
for chave, valor in receita.items():
    print(f'{chave} = {valor}')
""")
for chave, valor in receita.items():
    print(f'{chave} = {valor}')

# Soma, máximo, mínimo e tamanho:
print('\nSoma, máximo, mínimo e tamanho:')
print('sum(receita.values()): ', sum(receita.values()))
print('max(receita.values()): ', max(receita.values()))
print('min(receita.values()): ', min(receita.values()))
print('len(receita.values()): ', len(receita.values()))


