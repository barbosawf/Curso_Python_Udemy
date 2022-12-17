"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Default Dict -> Ao criar um dicionário, informa-se um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.
"""

# Recaptulando dicionários
print('Recaptulando dicionários')
dicionario = {'curso': 'Programação em Python'}

print('dicionario: ', dicionario)

print("\ndicionario['curso']: ", dicionario['curso'])

print("\ndicionario['outro']: ", 'KeyError, pois não tem a chave.')

# Fazendo o import
print('\nFazendo o import.')
from collections import defaultdict
print('from collections import defaultdict')

dicionario = defaultdict(lambda: 0)
print('\ndicionario = defaultdict(lambda: 0)')

print('\ndicionario: ', dicionario)

print("\ndicionario['curso'] = 'Programação em Python: Essencial'")
dicionario['curso'] = 'Programação em Python: Essencial'

print('\ndicionario: ', dicionario)

print("\ndicionario['curso']: ", dicionario['curso'])

print("\ndicionario['outro']: ", dicionario['outro'])
