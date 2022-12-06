"""
ranges
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas.

Formas gerais:

Forma 01
range(valor de parada)
OBS: valor de parada não incluso (início padrão é 0 e o passo é de 1).

Forma 02
range (valor inicial, valor de parada)
OBS: valor de parada não incluso (início especificado pelo usuário, e passo de 1 em 1).

Forma 03
range (valor inicial, valor de parada, passo)
OBS: valor de parada não incluso (início especificado pelo usuário, e passo especificado pelo usuário).

Forma 04
range (valor inicial, valor de parada, passo inverso)
OBS: valor de parada não incluso (início especificado pelo usuário, e passo especificado pelo usuário).

"""

# Forma 01
print('Forma 01')
for i in range(5):
    print(i)

# Forma 02
print('Forma 02')
for i in range(4, 11):
    print(i)

# Forma 03
print('Forma 03')
for i in range(0, 11, 2):
    print(i)

# Forma 04
print('Forma 03')
for i in range(10, 0, -2):
    print(i)

"""
Impressão de range: precisa colocar como lista.
"""

print(range(5))

print(list(range(5)))