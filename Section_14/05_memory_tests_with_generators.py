"""
Teste de memória com generators
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'


# Sequencia de fibonat usando listas
print(f'{a}Sequencia de fibonat usando listas{c}')


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


print(f"""{b}
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums{c}
""")

print('fib_lista(10): ', fib_lista(10))


# Sequencia de fibonat usando geradores
print(f'{a}Sequencia de fibonat usando geradores{c}')


def fib_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b, = b, a + b
        yield a
        cont += 1


print(f"""{b}
def fib_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b, = b, a + b
        yield a
        cont += 1 {c}
""")

print('list(fib_gen(10)): ', list(fib_gen(10)))