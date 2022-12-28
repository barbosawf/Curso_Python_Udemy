"""
Listas aninhadas
- Algumas linguagens de programação possuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (arrays/vetores);
    - Multidimensionais (matrizes);

Em Python se tem listas;

numeros = [1, 2, 3, 4, 5]
lista = [1, 'b', 3.234, True, 5]
"""

# Exemplo 01
print('Exemplo 01')

print('listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]')
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Equivalente à matriz 3 x 3 em outras linguagens

print('type(listas): ', type(listas))

print('\nlinha 0, coluna 1')
print('listas[0][1]: ', listas[0][1])

# Iterando com loops em uma lista aninhada
print('\nIterando com loops em uma lista aninhada')

print("""
for i in listas:
    for j in i:
        print(f'{j}', end=' ')
        """)
for i in listas:
    for j in i:
        print(f'{j}', end=' ')
print('')

# List Comprehention
print('\nList Comprehention')

print("\n[[print(valor, end=' ') for valor in lista] for lista in listas]")
[[print(valor, end=' ') for valor in lista] for lista in listas]
print('')

# Gerando um tabuleiro/matriz 3 x 3
print('\nGerando um tabuleiro/matriz 3 x 3')
tabuleiro1 = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
tabuleiro2 = [[numero for numero in range(5, 8)] for valor in range(1, 4)]

print('\ntabuleiro1 = [[numero for numero in range(1, 4)] for valor in range(1, 4)]')
print('tabuleiro1: ', tabuleiro1)

print('\ntabuleiro2 = [[numero for numero in range(4, 8)] for valor in range(1, 4)]')
print('tabuleiro2: ', tabuleiro2)

# Gerando jogadas do jogo da velha
print('\nGerando jogadas do jogo da velha')

velha = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)] for valor in range(1, 4)]
print("velha = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)] for valor in range(1, 4)]")

print('velha: ', velha)

# Gerando valores iniciais
print('\nGerando valores iniciais')
print([['*' for i in range(1, 4)] for j in range(1, 4)])
