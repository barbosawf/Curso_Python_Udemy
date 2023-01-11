"""
Dunder Name e Dunder Main

Dunder -> Double Underline

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunder parra criar funções, atributos, propriedade e entre outros utilizando
double Under para não gerar conflito com os nomes desses elementos na programação.

# Em Python se executarmos um módulo Python diretamente na linha de comando, internamente, o Python
atribuirá á variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.
"""

a = '\033[0;36;0m'
b = '\033[0;30;0m'
print('dir(): ', dir())

print('__name__: ', __name__)


from functions_with_parameters import soma_impares2

print(f'{b}from functions_with_parameters import soma_impares2{b}')

print('soma_impares2([1, 2, 3, 4, 5, 6, 7]): ', soma_impares2([1, 2, 3, 4, 5, 6, 7]))
print('\033[0;32;0m Verde.')
