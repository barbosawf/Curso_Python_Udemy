"""
Modulo Collections — Counter

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance container datetypes

Listas, tuplas, dicionários são conhecidos como containers (porque contém dados).

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento.
"""

# Realizando o import
print('Realizando o import: ')
print("from collections import Counter")

from collections import Counter

# Pode-se utilizar qualquer iterável (aqui utilizamos listas)
print('Pode-se utilizar qualquer iterável (aqui utilizamos listas):')
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 32, 32, 11, 11, 11, 54, 54, 54, 54, 54, 54, 54, 9, 9, 8, 7, 7, 7, 7]

# Utilizando o Counter
print('\nUtilizando o Counter: ')
res = Counter(lista)
print('\nres = Counter(lista):')
print('type(res): ', type(res))
print('res: ', res)

# Counter com uma string:
print('\nCounter com uma string:')

print("Counter('Geek University'): ", Counter('Geek University'))

# Exemplo 3
print('Exemplo 3')

texto = """Joaquim Marques Lisboa, Marquês de Tamandaré foi um militar da Armada Imperial Brasileira, onde atingiu o 
posto de Almirante. Ao longo da sua carreira, que durou quase 60 anos, participou na Guerra da Independência do 
Brasil, nos conflitos internos subsequentes no Período Regencial, e mais tarde nas guerras do Prata e do Paraguai. 
Pelos serviços prestados à sua pátria, foi feito Marquês e, mais tarde, foi escolhido como Patrono da Marinha do 
Brasil. Seu nome se encontra no Livro dos Heróis da Pátria. """

print(texto)

palavras = texto.split()

print('palavras = texto.split()')

res = Counter(palavras)

print('res = Counter(palavras)')
print('\nres: ', res)

print('\nres.most_common(5):', res.most_common(5))