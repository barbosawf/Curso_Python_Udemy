"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplismente Lambdas, são funções sem nome, ou seja, funções anônimas.


"""

# Exemplo de função em Python

print('Exemplo de função em Python')


def funcao(x):
    return 3 * x + 1


print("""
def funcao(x):
    return 3 * x + 1
    """)
print('funcao(4): ', funcao(4))

# Exemplo de Expressão Lambda

print('\nExemplo de Expressão Lambda')

lambda x: 3 * x + 1

print('lambda x: 3 * x + 1')

# Exemplo 01. Como utilizar a Expressão Lambda?

print('\nExemplo 01. Como utilizar a Expressão Lambda')

calc = lambda x: 3 * x + 1

print('calc = lambda x: 3 * x + 1')
print('calc(4): ', calc(4))

# Exemplo 02. Pode-se ter expressões lambdas com múltiplas entradas.
print('\nExemplo 02. Pode-se ter expressões lambdas com múltiplas entradas.')

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print("nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()")
print("nome_completo('geek ', ' university'):    ", nome_completo('geek ', ' university'))
print("nome_completo('ANGELINA ', ' jolie    '): ", nome_completo('ANGELINA ', ' jolie    '))

# Exemplo 03. Pode-se ter expressões lambdas com nenhuma entrada.
print('\n# Exemplo 03. Pode-se ter expressões lambdas com nenhuma entrada.')

amar = lambda: 'Como não amar Python?'
uma_entrada = lambda x: 3 *x + 1
duas_entradas = lambda x, y: (x * y) ** 0.5
tres_entradas = lambda x, y, z: (x * y) ** z

print("""
amar = lambda: 'Como não amar Python?'
uma_entrada = lambda x: 3 *x + 1
duas_entradas = lambda x, y: (x * y) ** 0.5
tres_entradas = lambda x, y, z: (x * y) ** z
""")

print('amar():                           ', amar())
print('uma_entrada(6):                   ', uma_entrada(6))
print('duas_entradas(5, 7).__round__(2): ', duas_entradas(5, 7).__round__(2))
print('tres_entradas(3, 4, 2):           ', tres_entradas(3, 4, 2))

# Exemplo 04
print('\nExemplo 04')

nome = 'Isaac Asimov'
print('nome: ', nome)
print("nome.split(' ')[-1].lower(): ", nome.split(' ')[-1].lower())

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print('\nautores: ', autores)

print("autores.sort(key=lambda nomes: nomes.split(' ')[-1].lower()): ")
autores.sort(key=lambda nomes: nomes.split(' ')[-1].lower())

print('autores: ', autores)

# Exemplo 05
print('\nExemplo 05')


def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = ax^2 + bx + c
    """
    return lambda x: a * x ** 2 + b * x + c


funcao_quadratica = geradora_funcao_quadratica(2, 3, -5)

print('''
def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = ax^2 + bx + c
    """
    return lambda x: a * x ** 2 + b * x + c


funcao_quadratica = geradora_funcao_quadratica(2, 3, -5)
''')

print('funcao_quadratica(0): ', funcao_quadratica(0))
print('funcao_quadratica(1): ', funcao_quadratica(1))
print('funcao_quadratica(2): ', funcao_quadratica(2))

print('\ngeradora_funcao_quadratica(2, 3, -5)(0): ', geradora_funcao_quadratica(2, 3, -5)(0))
print('geradora_funcao_quadratica(2, 3, -5)(1): ', geradora_funcao_quadratica(2, 3, -5)(1))
print('geradora_funcao_quadratica(2, 3, -5)(2): ', geradora_funcao_quadratica(2, 3, -5)(2))
