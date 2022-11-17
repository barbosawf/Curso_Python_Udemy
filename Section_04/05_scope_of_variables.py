"""
Escopo de variáveis
Qual é o escolpo dessa variável abaixo entre as barras?
|                              |
Dois casos de escopo:
1 - Variáveis globais:
    - Seu escopo compreende todo o programa.

2 - Variáveis locais:
 - São reconhecidas apenas no bloco onde foram declaradas, ou seja,
 seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python, fazemos:
nome_da_variavel = valor da variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declaramos uma variável,
nós não colocamos o tipo de dado dela. O tipo é finferido ao atribuírmos o valor à mesma
"""

num = 42

print(num)
print(type(num))

if num < 10:
    novo = num + 10
    print(novo)

print(novo) # dá erro porque ela não foi criada