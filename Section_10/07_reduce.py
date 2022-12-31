"""
A função reduce() não é mais uma função integrada (built-in). Ela precisa ser importada do módulo 'functools'.

Imagine o seguinte:

dados = [a1, a2, a3, ..., an]

def funcao(x,y):
    return x * y

reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função no resultado do Passo 1 mais o terceiro elemento.
    Passo 3: res3 = f(res2, a4) # Aplica a função no resultado do Passo 2 mais o quarto elemento.
    ...
    Passo n-1: res_n-1 = f(res_n-2, an).
"""

# Exemplo. Utilizar a função reduce para multiplicar todos os numeros de uma lista.
print('Exemplo. Utilizar a função reduce para multiplicar todos os numeros de uma lista.')


from functools import reduce


def mult(x, y):
    return x * y


print("""
from functools import reduce


def mult(x, y):
    return x * y
    """)


dados = [1, 2, 3, 5, 7, 5, 6, 2, 7, 9]

print('dados: ', dados)
print('reduce(mult, dados): ', reduce(mult, dados))
