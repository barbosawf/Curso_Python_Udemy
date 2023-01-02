"""
Módulo Random e o que são módulos?
- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo ramdom -> possui várias funções ára geração de números aleatórios

Forma 01 - Importação de módulo (todas as funções, atributos, classes e propriedades estarão prontos para uso.)

import random

dir(random)
"""
# Forma 01 — Importação de módulo (todas as funções, atributos,
#            classes e propriedades estarão prontos para uso)

print('Forma 01 - Importação de todo o módulo (todas as funções, atributos, '
      'classes e propriedades estarão prontos para uso)')

import random

# Aperte control, posicione o botão do 'mouse' em cima da palavra random e clique.
# Abrirá a documentação do módulo random.

# print(dir(random))

# help(random.random)

print(random.random())  # digita-se o nome do módulo.função()

# Forma 02 — Importação de uma função específica do módulo.
print('\nForma 02 — Importação de uma função específica do módulo.')

# Exemplo 01
print('\nExemplo 01')

print("""
from random import random

for i in range(10):
    if i < 9:
        print(round(random(), 2), end=', ')
    else:
        print(round(random(), 2))
        """)

from random import random

for i in range(10):
    if i < 9:
        print(round(random(), 2), end=', ')
    else:
        print(round(random(), 2))

# Exemplo 02
print('\nExemplo 02')

print("""
from random import uniform

for i in range(10):
    if i < 9:
        print(round(uniform(1, 5), 2), end=', ')
    else:
        print(round(uniform(1, 5), 2))  # 5 nunca é incluído
""")

from random import uniform

for i in range(10):
    if i < 9:
        print(round(uniform(1, 5), 2), end=', ')
    else:
        print(round(uniform(1, 5), 2))  # 5 nunca é incluído

# Exemplo 03
print('\nExemplo 03')

print("""
from random import randint

for i in range(6):
    if i < 5:
        print(randint(1, 60), end=', ')
    else:
        print(randint(1, 60))  # O 61 não é incluído
        """)

from random import randint

for i in range(6):
    if i < 5:
        print(randint(1, 60), end=', ')
    else:
        print(randint(1, 60))  # O 61 não é incluído

# Exemplo 04
print('\nExemplo 04')

print('from random import choice')
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print('jogadas: ', jogadas)

print('choice(jogadas): ', choice(jogadas))

print("choice('Geek University'): ", choice('Geek University'))

# Exemplo 05
print('\nExemplo 05')

print('from random import shuffle')
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4']
print('cartas: ', cartas)
shuffle(cartas)
print('shuffle(cartas): ')
print('cartas: ', cartas)
