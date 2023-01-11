"""
Módulos Customizados

Todos os arquivos que criamos neste curso são módulos Python prontos para serem utilizados.

"""
# Exemplo 01. Importação o módulo inteiro.
print('\nExemplo 01.  Importação o módulo inteiro.')

import functions_with_parameters as fp
print('import functions_with_parameters')
print('fp.soma_todos_numeros(1, 2, 3, 4, 5): ', fp.soma_todos_numeros(1, 2, 3, 4, 5))

# Exemplo 02. Importação de funções específicas.
print('\nExemplo 02. Importação de funções específicas.')

from functions_with_parameters import quadrado, soma_todos_numeros, soma_impares2
print('from functions_with_parameters import quadrado, soma_impares2')
print('soma_impares2([1, 2, 3, 4, 5, 6, 7, 8, 9]): ', soma_impares2([1, 2, 3, 4, 5, 6, 7, 8, 9]))
