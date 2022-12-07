"""
Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 — As tuplas são representadas por parênteses ();
2 - As tuplas são imutáveis. Isso significa que ao se criar uma tupla ela não muda.
    Toda operação em uma tupla gera uma nova tupla.
"""
# Tipo
print('Tipo:')
print('type(()): ', type(()))

# CUIDADO 1 — As tuplas são representadas por parênteses, mas podem ser construídas sem eles:
print('\nCUIDADO 1 - As tuplas são representadas por parênteses, mas podem ser construídas sem eles:')
tupla1 = (1, 2, 3, 4, 5, 6)
print('tupla1 = (1, 2, 3, 4, 5, 6)')
print('type(tupla1): ', type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print('\ntupla2 = 1, 2, 3, 4, 5, 6')
print('type(tupla2): ', type(tupla2))

# CUIDADO 2 — Tuplas com 1 elemento:
print('\nCUIDADO 2 - Tuplas com 1 elemento:')
tupla3 = (5)
print('tupla3 = (5)')
print('type(tupla3): ', type(tupla3),  'NÃO É UMA TUPLA!')

tupla4 = (5,)
print('\ntupla4 = (5,)')
print('type(tupla4): ', type(tupla4),  'É UMA TUPLA!')

tupla5 = 5,
print('\ntupla5 = 5,')
print('type(tupla5): ', type(tupla5),  'É UMA TUPLA!')

# PODEMOS CONCLUIR QUE TUPLAS SÃO DEFINIDAS PELA VÍRGULA E NÃO PELOS PARÊNTESES.
print('\nPODEMOS CONCLUIR QUE TUPLAS SÃO DEFINIDAS PELA VÍRGULA E NÃO PELOS PARÊNTESES.')

# Podemos gerar uma tupla dinamicamente com os comandos range() e tuple():
print('\nPodemos gerar uma tupla dinamicamente com os comandos range() e tuple():')
tupla = tuple(range(11))
print('tupla = tuple(range(11))')
print('tupla: ', tupla)
print('type(tupla): ', type(tupla))

# Desempacotamento de tupla:
print('\nDesempacotamento de tupla:')
tupla = ('Geek University', 'Programação em Python: Essencial!')
print("tupla = ('Geek University', 'Programação em Python: Essencial!')")
escola, curso = tupla
print('escola, curso = tupla')
print('escola: ', escola)
print('curso: ', curso)

# Métodos para adição e remoção de elementos naas tuplas não existem, pois, são imutáveis.
print('\nMétodos para adição e remoção de elementos naas tuplas não existem, pois são imutáveis.')

# Soma, máximo, mímimo e tamanho.
print('\nSoma, máximo, mímimo e tamanho.')
tupla = 1, 5, 7, 3, 5, 9
print('tupla: ', tupla)
print('sum(tupla): ', sum(tupla))
print('max(tupla): ', max(tupla))
print('min(tupla): ', min(tupla))
print('len(tupla): ', len(tupla))

# Concatenar tuplas:
print('\nConcatenar tuplas:')
tupla1 = 1, 2, 3
tupla2 = 4, 5, 6
print('tupla1:           ', tupla1)
print('tupla2:           ', tupla2)
print('tupla1 + tupla 2: ', tupla1 + tupla2)
print('tupla1:           ', tupla1)
print('tupla2:           ', tupla2)

# Verificar se determinado elemento está contido na tupla:
print('\nVerificar se determinado elemento está contido na tupla:')
tupla = 1, 2, 3
print('tupla:      ', tupla)
print('2 in tupla: ', 2 in tupla)
print('5 in tupla: ', 5 in tupla)

# Iterar sobre uma tupla:
print('\nIterar sobre uma tupla:')

tupla = 1, 2, 3
print('tupla:      ', tupla)

print("""
for n in tupla:
    print(n)
""")
for n in tupla:
    print(n)


print("""
for i, n in enumerate(tupla):
    print(i, n)
""")
for i, n in enumerate(tupla):
    print(i, n)

# Contar elementos dentro de uma tupla:
print('\nContar elementos dentro de uma tupla:')
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print('tupla:            ', tupla)
print("tupla.count('a'): ", tupla.count('a'))
print("tupla.count('c'): ", tupla.count('c'))

escola = tuple('Geek University')
print("\nescola = tuple('Geek University'): ")
print("escola: ", escola)
print("escola.count('e'): ", escola.count('e'))

# Dicas na utilização de tuplas:

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos numa coleção.

# Exemplo 1

print("""
Dicas na utilização de tuplas:
Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.
""")
print('Exemplo 1')
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print('meses: ', meses)

# Acesso a elementos de uma tupla:
print('\nAcesso a elementos de uma tupla:')
print('meses:    ', meses)
print('meses[2]: ', meses[2])

# Iterar com while:
print('\nIterar com while:')

print("""
i = 0
while i < len(meses):
    print(meses[i])
    i += 1
""")
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar em qual índice um elemento está na tupla:
print('\nVerificar em qual índice um elemento está na tupla:')
print('meses:                ', meses)
print("meses.index('Março'): ", meses.index('Março'))

# Fatiamento (slicing):
print('\nFatiamento (slicing):')
print('meses:        ', meses)
print('meses[1]:     ', meses[1])
print('meses[2:]:    ', meses[2:])
print('meses[-3:]:   ', meses[-3:])
print('meses[:2]:    ', meses[:2])
print('meses[:-5]:   ', meses[:-5])
print('meses[1::2]:  ', meses[1::2])
print('meses[::2]:   ', meses[::2])
print('meses[1::-1]: ', meses[1::-1])

# Por que utilizar tuplas?

# Tuplas são mais rápidas do que listas.
# Tuplas deixam o seu código mais seguro devido à imutabilidade.

# Copiar uma tupla
print('\nCopiar uma tupla')
tupla = (1, 2, 3)
print('tupla: ', tupla)
nova = tupla
print('nova = tupla')
print('nova:  ', nova)
print('tupla: ', tupla)

# Na tupla não temos o problema de shalow copy

# Concatenar tuplas:
print('\nConcatenar tuplas:')
outra = (4, 5, 6)
print('tupla:         ', tupla)
print('outra:         ', outra)
print('tupla + outra: ', tupla + outra)
