"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays).
São DINÂMICOS:
    - Não possuem tamanho fixo, ou seja, podemos criar a lista e adicionar ou remover elementos, posteriormente.
    - Pode-se colocar QUALQUER dado, ou seja, não possuem dado fixo.
São representadas por chochetes: []
"""
# Printando os tipos
print('Printando os tipos. Uso do comando type():')
print('type(3):         ', type(3))
print('type(True):      ', type(True))
print("type('a'):       ", type('a'))
print('type([]):        ', type([]))
print('type([1, 2, 4]): ', type([1, 2, 4]))

# Listas
print('\nListas:')
l1 = [1, 3, 44, 26, 5]
l2 = ['G', 'e', ' ', 'v']
l3 = []
l4 = list(range(11))
l5 = list('Geek University')

print('l1: ', l1)
print('l2: ', l2)
print('l3: ', l3)
print('l4: ', l4)
print('l5: ', l5)

# Checar se um determinado valor está contido na lista:
print('\nPodemos checar se um determinado valor está contido na lista. \nExemplo 01')
print("num = int(input('Qual o número você quer enontrar na lista 4? '))\n"
      "if num in l4:\n"
      "    print(f'Encontrei o número {num}!')\n"
      "else:\n"
      "    print(f'Não encontrei o número {num}!')\n")
num = int(input('Qual o número você quer enontrar na lista 4? '))
if num in l4:
    print(f'Encontrei o número {num}!')
else:
    print(f'Não encontrei o número {num}!')

print('\nPodemos checar se um determinado valor está contido na lista. \nExemplo 02')
print("letra = str(input('Qual a letra você quer enontrar na lista 5? ')).strip()\n"
      "if letra in l5:\n"
      "    print(f'Encontrei a letra {letra}!')\n"
      "else:\n"
      "    print(f'Não encontrei a letra {letra}!')")
letra = str(input('Qual a letra você quer enontrar na lista 5? ')).strip()
if letra in l5:
    print(f'Encontrei a letra {letra}!')
else:
    print(f'Não encontrei a letra {letra}!')

# Ordenar uma lista através da função sort()
print('\nPodemos ordenar uma lista através da função .sort(). \nEx.:')
print('l1.sort()')
l1.sort()
print(l1)

# Contar o número de ocorrências de um valor numa lista através do comando count()
print('\nPodemos contar o número de ocorrências de um valor em uma lista com o comando .count(). \nEx.:')
print("l5:           ", l5)
print("l5.count('e'):", l5.count('e'))

# Adicionar elementos em listas (função append)
# OBS.: Com append, adiciona-se um elemento por vez.
print('\nAdicionar elementos em listas com a função .append().'
      ' Neste caso, adiciona-se um elemento por vez.')
print('l1:            ', l1)
l1.append(41)
print('l1.append(41): ', l1)

# É possível adicionar uma lista numa lista, pois conta como elemento.
print('\nÉ possível adicionar uma lista numa lista, pois conta como elemento. \nEX.:')

print('l4:                     ', l4)
l4.append([9, 10, 11])
print('l4.append([9, 10, 11]): ', l4)

# É possível encontrar um elemento na lista.
print("\nÉ possível encontrar um elemento na lista.")
print("\n"
      "if [9, 10, 11] in l1:\n"
      "    print('Encontrei a lista!')\n"
      "else:\n"
      "    print('Não encontrei a lista!')")
if [9, 10, 11] in l4:
    print('Encontrei a lista!')
else:
    print('Não encontrei a lista!')

print("\n"
      "if [9, 11] in l1:\n"
      "    print('Encontrei a lista!')\n"
      "else:\n"
      "    print('Não encontrei a lista!')")
if [9, 11] in l1:
    print('Encontrei a lista!')
else:
    print('Não encontrei a lista!')

# Adicionar elementos iteráveis (ex.: listas) dentro de uma lista com a função extend():
print('\nAdicionar elementos iteráveis (ex.: listas) dentro de uma lista com a função .extend():')
print('Exemplo 01:')
print('l4:                       ', l4)
l4.extend([123, 41, 67])  # A função extend só aceita elementos iteráveis (devem formar uma lista)
print('l4.extend([123, 41, 67]): ', l4)

print(
    '\n'
    'l4.extend(22) # Não aceita\n'
    'print(l4)'
)

print('\nExemplo 02:')
print('l4:              ', l4)
l4.extend([22])
print('l4.extend([22]): ', l4)

print('\nExemplo 03:')
print('l4:              ', l4)
l4.extend('Geek')  # 'Geek' é um elemento iterável.
print("l4.extend('Geek'): ", l4)

# Podemos inserir um novo elemento na lista informando a posição do índice.
# Não substitui o valor inicial. O valor que estava na posição é deslocado para dreita.
print("""
\nPodemos inserir um novo elemento na lista informando a posição do índice.
Não substitui o valor inicial. O valor que estava na posição é deslocado para dreita.
"""
      )
print('l1:                         ', l1)
l1.insert(2, 'Novo valor')
print("l1.insert(2, 'Novo valor'): ", l1)

# Podemos juntar listas pelo comando +
print('\nJunção da l1 com a l2 através do comando +: \nEx.:l6 = l1 + l2')
l6 = l1 + l2
print(l6)

"""
# Podemos juntar listas pelo comando .extend
print('\nJunção da l1 com a l2 através do comando extend: l6 = l1 + l2')
l1.extend(l2)
print(l1)
"""

# Revertendo uma lista através do comando reverse
print('\nRevertendo uma lista através do comando .reverse(). \nEx.:l2.reverse()')
l2.reverse()
print(l2)

# Revertendo uma lista através da indicação da posição dos elementos nela contidos
print('\nRevertendo uma lista através da indicação da posição dos elementos nela contidos. \nEx.: l4[::-1]')
print(l4[::-1])

# Copiar uma lista
print('\nCopiando uma lista através do comando .copy(). \nEx.: l7 = l4.copy()')
l7 = l4.copy()
print(l7)

# Tamanho de uma lista
print('\nTamanho de uma lista pode ser acessado pelo comando len(). \nEx.: len(l1)')
print(len(l1))

# Remover o último elemento de uma lista através do comando .pop(). Ex.: l5.pop()
print('\nRemover o último elemento de uma lista através do comando .pop(). \nEx.: l5.pop()')
print('l5:       ', l5)
l5.pop()
print('l5.pop(): ', l5)

# Remover um elemento pelo índice através do comando .pop(). Ex.: l1.pop(3)
print('\nRemover um elemento pelo índice através do comando .pop(). Ex.: l1.pop(3)')
print('l1:        ', l1)
l1.pop(3)
print('l1.pop(3): ', l1)
l1.pop(3)
print('l1.pop(3): ', l1)

# Remover todos os elementos de uma lista através do comando .clear(). Ex.: l1.clear()
print('\nRemover todos os elementos de uma lista através do comando .clear(). Ex.: l1.clear()')
print('l1:         ', l1)
l1.clear()
print('l1.clear(): ', l1)

# Repetir os elementos da lista utilizando o sinal da multiplicação (*). Ex.: l2 * 3:
print('\nRepetir os elementos da lista utilizando o sinal da multiplicação (*). Ex.: l2 * 3:')
print('l2:     ', l2)
print('l2 * 3: ', l2 * 3)

# Converter uma ‘string’ para uma lista:
print('\nConverter uma string para uma lista:')
print('\nExemplo 01 - utilizando o comando .split():')
curso = 'Programação em Python: Essencial!'
print('curso:                 ', curso)
curso = curso.split()  # default separa por espaço
print('curso = curso.split(): ', curso)

print('\nExemplo 02 - utilizando o comando .split() com definição do separador:')
curso = 'Programação em Python: Essencial!'
print('curso:                    ', curso)
curso = curso.split(':')  # default separa por espaço
print("curso = curso.split(':'): ", curso)

# Tranformar uma lista numa ‘string’ com o comando join():
print('\nTransformar uma lista numa string com o comando join():')
l9 = ['Programação', 'em', 'Python', 'Essencial']
print('\nExemplo 01:')
print('l9:           ', l9)
print("' '.join(l9): ", ' '.join(l9))
print('\nExemplo 02:')
print('l9:           ', l9)
print("'$'.join(l9): ", '$'.join(l9))

# Colocar qualquer dado numa lista.
print('\nColocar qualquer dado numa lista:')
l10 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 46546549845564]
print('l10:       ', l10)
print('type(l10): ', type(l10))

# Iterando sobre listas:
print('\nIterando sobre listas:\nExemplo 01:')
l11 = [1, 4, 7, 0, 'Geek']
print('l11: ', l11)
print("\n"
      "for i in l11:\n"
      "    print(i)\n")

for i in l11:
    print(i)

print('\nExemplo 02:')

print('l5: ', l5)
print("\n"
      "soma = ''\n"
      "for i in l5:\n"
      "    soma = soma + i\n"
      "print(soma)\n")

soma = ''
for i in l5:
    soma = soma + i
print(soma)

print('\nExemplo 03:')

print(
    """
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na sacola [digite 'sair' para sair]: ")
    produto = str(input()).lower().strip()
    if produto != 'sair':
        carrinho.append(produto)

print('\nProdutos na sacola: ')

for produto in carrinho:
    print(produto)
"""
)

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na sacola [digite 'sair' para sair]: ")
    produto = str(input()).lower().strip()
    if produto != 'sair':
        carrinho.append(produto)

print('\nProdutos na sacola: ')
for produto in carrinho:
    print(produto)

# Variáveis podem ser adicionadas em listas desde que sejam previamente declaradas:
print('\nVariáveis podem ser adicionadas em listas desde que sejam previamente declaradas:')
num1 = 1
num2 = 2
num3 = 3

print("""
num = 1
num = 2
num = 3\n""")

numeros = [num1, num2, num3]

print('[num1, num2, num3]: ', numeros)

# Em lista se faz o acesso aos elementos de forma indexada:
print('\nEm lista se faz o acesso aos elementos de forma indexada:')
cores = ['verde', 'amarelo', 'vermelho', 'azul']
print('cores:         ', cores)
print('cores[0]:      ', cores[0])
print('cores[2]:      ', cores[2])
print('cores[2][2:4]: ', cores[2][2:4])

# Em lista se pode fazer o acesso aos elementos de forma reversa pela indexação:
print('\nEm lista se pode fazer fazer o acesso aos elementos de forma reversa pela indexação:')
cores = ['verde', 'amarelo', 'vermelho', 'azul']
print('cores:          ', cores)
print('cores[-1]:      ', cores[-1])
print('cores[-2]:      ', cores[-2])
print('cores[-3][2:4]: ', cores[-3][2:4])

# Mais exemplos de iterações:
print('\nMais exemplos de iteração:')
print('\nExemplo 01:')
print('cores: ', cores)

print("""
for cor in cores:
    print(cor)
""")

for cor in cores:
    print(cor)

print('\nExemplo 02:')
print('cores: ', cores)

print("""
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1
""")

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar índice em um for:
print('\nGerar índice em um for:')

print("""
for i, cor in enumerate(cores):
    print(i, cor)\n""")
for i, cor in enumerate(cores):
    print(i, cor)

print('\nlist(enumerate(cores)): ', list(enumerate(cores)))

# Listas aceitam valores repetidos:
print('\nListas aceitam valores repetidos:')
l12 = []
print('l12: ', l12)
l12.append(23)
l12.append(23)
l12.append(55)
l12.append(55)
print("""
l12.append(23)
l12.append(23)
l12.append(55)
l12.append(55)\n""")

print('l12: ', l12)

# Métodos não tão importantes mas também úteis:
print('\nMétodos não tão importantes mas também úteis: ')

# Econtrar o índice de um elemento na lista com o comando index():
print('\nEcontrar o índice de um elemento na lista com o comando index(): ')
numeros = [5, 6, 7, 8, 9, 10]
print('numeros:          ', numeros)
print('numeros.index(6): ', numeros.index(6))
print('numeros.index(9): ', numeros.index(9))  # erro se o elemento não estiver na lista
