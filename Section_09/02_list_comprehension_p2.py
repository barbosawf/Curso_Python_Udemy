"""
List Comprehention

Pode-se adicionar estruturas condicionais lógicas numa List Comprehension
"""
from typing import List

# Exemplo 01
print('Exemplo 01')

numeros = [1, 2, 3, 4, 5, 6]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print("""
numeros = [1, 2, 3, 4, 5, 6]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

""")

print('pares: ', pares)
print('impares: ', impares)

# Exemplo 02
print('\nExemplo 02')

# O resto da divisão por 2 é 0 e 0 em Python é False. not False = True. Impar é o oposto.

print('O resto da divisão por 2 é 0 e 0 em Python é False. not False = True. Impar é o contrário.')

pares = [num for num in numeros if not num % 2]
impares = [num for num in numeros if num % 2]

print("""
pares = [num for num in numeros if not num % 2]
impares = [num for num in numeros if num % 2]
""")

print('pares: ', pares)
print('impares: ', impares)

# Exemplo 03
print('\nExemplo 03')

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]

print('res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]')
print('res: ', res)
