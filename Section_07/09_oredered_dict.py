"""
OrderedDict
https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""
# Em um dicionário, a ordem de inserção dos elementos não é garantida.
print('Em um dicionário, a ordem de inserção dos elementos não é garantida.')

dicionario = {'f': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 0}
print('dicionario: ', dicionario)

print("""
for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')
""")
for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

# Fazendo o import
print('\nFazendo o import.')
from collections import OrderedDict
print('from collections import OrderedDict')

dicionario = OrderedDict({'f': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 0})

print('\ndicionario: ', dicionario)

print("""
for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')
""")
for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

# Entendendo a diferença entre Dict e Ordered Dict
print('\nEntendendo a diferença entre Dict e Ordered Dict')

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print('dict1: ', dict1)
print('dict2: ', dict2)
print('dict1 == dict2: ', dict1 == dict2)
print('True porque a ordem dos elementos NÃO importa para o dicionário ordenado.')

dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print('\ndict1: ', dict1)
print('dict2: ', dict2)
print('dict1 == dict2: ', dict1 == dict2)
print('False porque a ordem dos elementos importa para o dicionário.')