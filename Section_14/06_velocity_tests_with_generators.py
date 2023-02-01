"""
Teste de velocidade com Expressões Geradoras
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Generators (Geradores)
print(f'{a}Generators (Geradores){c}')


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(f"""{b}
def nums():
    for num in range(1, 10):
        yield num

ge1 = nums(){c}
""")

print('ge1: ', ge1)  # Generator
print('next(ge1): ', next(ge1))
print('next(ge1): ', next(ge1))


# Generator Expression
print(f'\n{a}Generator Expression (Expressão Geradora){c}')

print(f'{b}\nge2 = (num for num in range(1, 10))\n{c}')

ge2 = (num for num in range(1, 10))

print('ge2: ', ge2)  # Generator
print('next(ge2): ', next(ge2))
print('next(ge2): ', next(ge2))


# Soma em Generator Expression
print(f'\n{a}Soma em Generator Expression{c}')

print(f'{b}\ns = sum(num for num in range(1, 10))\n{c}')

s = sum(num for num in range(1, 10))

print('s: ', s)


# Realizando o teste de velocidade
print(f'{a}Realizando o teste de velocidade{b}')

import time
print(f'\n{b}import time{c}')

# Teste com Generator Expression
print(f'{a}\nTeste com Generator Expression{b}')

get_start = time.time()

sum(num for num in range(100000000))

get_end = time.time()

print(f"""{b}
get_start = time.time()

sum(num for num in range(10000000))

get_end = time.time(){c}
""")

print('get_end - get_start: ', get_end - get_start)

print(f'{a}\nTeste com List Comprehension{b}')

get_start = time.time()

sum([num for num in range(100000000)])

get_end = time.time()

print(f"""{b}
get_start = time.time()

sum([num for num in range(100000000)])

get_end = time.time(){c}
""")

print('get_end - get_start: ', get_end - get_start)
