"""
Set Comprehension

"""

# Exemplo 01
print('Exemplo 01')

numeros = {num for num in range(1, 6)}
print('numeros = {num for num in range(1, 6)}')
print('numeros: ', numeros)

# Exemplo 02
print('\nExemplo 02')

numeros = {x ** 2 for x in range(0, 10)}
print('numeros = (x ** 2 for x in range(10))')
print('numeros: ', numeros)

# Desafio! Fazer uma alteração na estrutura acima para gerar um dicionário ao invés de set.
print('\n# Desafio! Fazer uma alteração na estrutura acima para gerar um dicionário ao invés de set.')

numeros = {x: x ** 2 for x in range(0, 10)}
print('numeros = (x: x ** 2 for x in range(10))')
print('numeros: ', numeros)

# Exemplo 03
print('\nExemplo 03')

letras = {letra for letra in 'Geek University'}
print("letras = {letra for letra in 'Geek University'}")
print('letras: ', letras)
print('Conjunto não mantém ordenação e não tém valores repetidos.')
