"""
Dunder Name e Dunder Main

Dunder -> Double Underline

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunder parra criar funções, atributos, propriedade e entre outros utilizando
double Under para não gerar conflito com os nomes desses elementos na programação.

# Em Python se executarmos um módulo Python diretamente na linha de comando, internamente, o Python
atribuirá á variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

Se um arquivo for executado diretamente o nome dele será __main__. __
Se for executado via importação o nome dele será o nome do arquivo.
"""

print('dir(): ', dir())

print('__name__: ', __name__)


from functions_with_parameters import soma_impares2

print(f'\nfrom functions_with_parameters import soma_impares2')
print('Verificar o módulo funções com parâmetros para ver o __name__ e __main__')

print('\nsoma_impares2([1, 2, 3, 4, 5, 6, 7]): ', soma_impares2([1, 2, 3, 4, 5, 6, 7]))

print('')
import primeiro
import segundo
