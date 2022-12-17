"""
Módulo Collections — Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Named Tupla → São tuplas diferenciadas nas quais especificamos um nome para a mesma e para os parâmetros.
"""

# Recaptulando tupla
print('Recaptulando tupla')
tupla = (1, 2, 4)

print('tupla: ', tupla)
print('tupla[1]: ', tupla[1])

# Fazendo o import
print('\nFazendo o import.')
from collections import namedtuple
print('from collections import namedtuple')

# Precisamos definir o nome e parâmetros
print('\nPrecisamos definir o nome e parâmetros')

# Forma 01 — Declaração Named Tuple
print('\nForma 01 - Declaração Named Tuple')

cachorro = namedtuple('cachorro', 'idade raca nome')
print("cachorro = namedtuple('cachorro', 'idade raca nome')")
print('cachorro: ', cachorro)

# Forma 02 — Declaração Named Tuple
print('\nForma 02 - Declaração Named Tuple')

cachorro = namedtuple('cachorro', 'idade, raca, nome')
print("cachorro = namedtuple('cachorro', 'idade, raca, nome')")
print('cachorro: ', cachorro)

# Forma 03 — Declaração Named Tuple
print('\nForma 03 - Declaração Named Tuple')

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])
print("cachorro = nnamedtuple('cachorro', ['idade', 'raca', 'nome'])")

# Usando a Named Tupla
print('\nUsando a Named Tupla')

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print("ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')")

print('ray: ', ray)

# Acesso a um elemento:
print('\nAcesso a um elemento: ')

# Forma 01
print('Forma 01')

print('ray[0]: ', ray[0])
print('ray[1]: ', ray[1])
print('ray[2]: ', ray[2])

# Forma 02
print('\nForma 02')

print('ray.idade: ', ray.idade)
print('ray.raca: ', ray.raca)
print('ray.nome: ', ray.nome)

# Qual é o índice?
print('\nQual é o índice?')
print("ray.index('Chow-Chow'): ", ray.index('Chow-Chow'))

# Contagem?
print('\nContagem')
print("ray.count('Chow-Chow'): ", ray.count('Chow-Chow'))
