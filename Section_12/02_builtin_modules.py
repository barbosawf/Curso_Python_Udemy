"""
Módulos Builtin
| Python | Módulos builtin |

https://docs.python.org/3/py-modindex.html
"""

# Exemplo 01. Módulos carregados ao abrir o Python
print('\nExemplo 01. Módulos carregados ao abrir o Python: ')
print('\ndir(): ', dir())

# Exemplo 02. Módulos carregados ao importar  determinados módulos builtin
print('\nExemplo 02. Módulos carregados ao importar determinados módulos builtin: ')

print('import random')
print('\ndir(): ', dir())

# Exemplo 03. Uso de apelido para os módulos
print('\n# Exemplo 03. Uso de apelido para os módulos.')

import statistics as stats
print('import statistics as stats')
print('\ndir(): ', dir())
print('\nstats.mean([2, 3, 4, 5]): ', stats.mean([2, 3, 4, 5]))

# Exemplo 04. Importação de todas as funções de um módulo utilizando o asterísco.
print('\nExemplo 04. Importação de todas as funções de um módulo utilizando o asterísco.')

from random import *
print('from random import *')
print('\ndir(): ', dir())
print('\nrandom(): ', random())

# Exemplo 05. Uso de apelido para as funções
print('\n# Exemplo 05. Uso de apelido para as funções.')

from random import randint as rdi, random as rdm
print('from random import randint as rdi')
print('rdi(5, 89): ', rdi(5, 89))
print('\nrdm(): ', rdm())

# Exemplo 06. Uso de tupla para colocar vários imports de um mesmo módulo.
print('\n# Exemplo 06. Uso de tupla para colocar vários imports de um mesmo módulo.')

print("""
from random import 
    (random,
     randint,
     shuffle,
     choice)
     """)
