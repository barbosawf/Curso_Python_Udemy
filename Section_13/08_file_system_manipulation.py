"""

"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

import os

# Descobrindo se um arquivo existe
print(f'{a}Descobrindo se um arquivo ou diretório existe{c}')

print("os.path.exists('arquivo.txt'): ", os.path.exists('arquivo.txt'))
print("os.path.exists('frutas.txt'): ", os.path.exists('frutas.txt'))

# Descobrindo se um arquivo ou diretório existe
print(f'\n{a}Descobrindo se um diretório relativo existe{c}')

print("os.path.exists('Directory_Example'): ", os.path.exists('Directory_Example'))
print("os.path.exists('Directory_Example/Directory_Example_02'): ",
      os.path.exists('Directory_Example/Directory_Example_02'))
print("os.path.exists('Directory_Example/Outro'): ",
      os.path.exists('Directory_Example/Outro'))

# Descobrindo se um arquivo ou diretório absoluto existe
print(f'\n{a}Descobrindo se um diretório absoluto existe{c}')

print("os.path.exists('D:\\PycharmProjects\\Udemy_Python\\Section_13'): ",
      os.path.exists('D:\\PycharmProjects\\Udemy_Python\\Section_13'))

# Criando arquivos (Forma 01)
print(f'\n{a}Criando arquivos (Forma 01){c}')
print(f"{b}open('arquivo_teste.txt', 'w').close():{c} ")
open('arquivo_teste.txt', 'w').close()

# Criando arquivos (Forma 02)
print(f'\n{a}Criando arquivos (Forma 02){c}')
print(f"{b}open('arquivo_teste2.txt', 'a').close():{c} ")
open('arquivo_teste2.txt', 'a').close()

# Criando arquivos (Forma 03)
print(f'\n{a}Criando arquivos (Forma 03){c}')
print(f"""{b}with open('arquivo_teste3.txt', 'a') as arquivo:
    pass{c}""")
with open('arquivo_teste3.txt', 'a') as arquivo:
    pass  # é para fazer nada

""" NÃO FUNCIONA NO WINDOWS, SÓ EM SISTEMAS COMO O LINUX E IOS
# Criando arquivos (Forma 04)
print(f'\\n{a}Criando arquivos (Forma 04){c}')
print(f"{b}os.mknod('arquivo_teste4.txt'):{c} ")
os.mknod("arquivo_teste4.txt")

print(f"zn{b}os.mknod('Directory_Example/university.txt'):{c} ")
os.mknod('Directory_Example/university.txt')
os.mknod()

Se criarmos um arquivo via mknod() e o arquivo já existir, teremos o erro FileExistsError
"""

# Criando um diretório
print(f'\n{a}Criando um diretório{c}')

print(f"""{b}
try:
    os.mkdir('Directory_Example/Directory_Example_03')
except FileExistsError:
    print('O diretório já existe'){c}
    """)

try:
    os.mkdir('Directory_Example/Directory_Example_03')
except FileExistsError as er:
    print(f'O diretório já existe: \n{er}')

print(f"""{b}
try:
    os.mkdir('Directory_Example/D_1/D_2/D_3')
except (FileNotFoundError, FileExistsError) as err:
    print('Na criação de diretórios, eles devem ser criados um a um:\\n'
          'Se o diretório anterior ao diretório que se quer criar não existir, o erro FileNotFoundError acontecerá.'
          '{'{err}'}')
          {c}""")

try:
    os.mkdir('Directory_Example/D_1/D_2/D_3')
except (FileNotFoundError, FileExistsError) as err:
    print(f'Na criação de diretórios, eles devem ser criados um a um:\n'
          f'Se o diretório anterior ao diretório que se quer criar não existir, o erro FileNotFoundError acontecerá.'
          f'\n{err}')


print(f"""{b}
try:
    os.makedirs('Directory_Example/D_1/D_2/D_3', exist_ok=True)  # exist_ok é para não dar erro. Não precisa do try.
except FileExistsError:
    print('O diretório já existe'){c}
    """)

try:
    os.makedirs('Directory_Example/D_1/D_2/D_3', exist_ok=True)  # exist_ok é para não dar erro. Não precisa do try.
except FileExistsError as er:
    print(f'Os diretórios já existem: \n{er}')

