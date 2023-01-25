"""
Entendendo Iterators e Iterables

Iterator:
    - um objeto que pode ser iterado.
    - um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;
Iterable:
    - um objeto que irá retornar um iterator quando a função iter() for chamada.
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Testando se são iterators
print(f'{a}UTestando se são iterators{c}')

nome = 'Geek'  # É um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator.

print(f"""{b}
nome     =      {nome}
numeros  = {numeros}{c}
""")

print(f"""{b}
try:
    next(nome)
except TypeError as er:
    print(er)
{c}""")

try:
    next(nome)
except TypeError as er:
    print(er)

print(f"""{b}
try:
    next(numeros)
except TypeError as er:
    print(er)
{c}""")

try:
    next(numeros)
except TypeError as er:
    print(er)


# Tornando os objetos em iterators
print(f'{a}Testando se são iterators{c}')

print(f"""{b}
it1 = iter(nome)
it2 = iter(numeros)
{c}""")

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
