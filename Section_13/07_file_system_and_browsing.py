"""
Sistema de arquivos e navegação

Para recorrer à manipulação de arquivos do sistema operacional, precisamos importar
e usar o módulo os.

os -> Operatinig System - Sistema operacional
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

import os

# Qual é o diretório corrente?
print(f'{a}Qual é o diretório corrente? {c}')

print('os.getcwd(): ', os.getcwd())  # Retorna o path absoluto

"""print(f"\n{b}os.chdir('..'){c}")
os.chdir('..')

print('\nos.getcwd(): ', os.getcwd())"""

# Verificação de diretório absoluto para sistemas Posix
print(f'\n{a}Verificação de diretório absoluto para sistemas Posix {c}')
print("\nos.path.isabs('/home/geek'): ", os.path.isabs('/home/geek'))

# Verificação de diretório absoluto para o sistema Windows
print(f'\n{a}Verificação de diretório absoluto para o sistema Windows  {c}')
print("\nos.path.isabs('C:\\Users\\geek'): ", os.path.isabs('C:\\Users\\geek'))
print(f'{b}Duas barras para verificação no Windows "\\" '
      f'porque apenas uma é um caracter de escape nos sistemas Posit{c}.')

# Podemos identificar o sistema operacional com o módulo os
print(f'{a}Podemos identificar o sistema operacional com o módulo os.{c}')
print('os.name: ', os.name)  # nt é Windows

"""
# Podemos ter mais detalhes do sistema operacional
print('os.uname(): ', os.uname())  # não tem no windons e não aparece, só para posix.
"""

# Podemos mudar o diretório através do python
print(f'\n{a}Podemos mudar o diretório através do python:{c}')

print('\nos.getcwd(): ', os.getcwd())

print(f"\n{b}res = os.path.join(os.getcwd(), 'Directory_Example'){c}")
res = os.path.join(os.getcwd(), 'Directory_Example')
print('\nres: ', res)

print(f'\n{b}os.chdir(res): {c}')
os.chdir(res)

print('\nos.getcwd(): ', os.getcwd())

print(f"{b}\nos.chdir('..') {c}")
os.chdir('..')

print('\nos.getcwd(): ', os.getcwd())

print(f"\n{b}res = os.path.join(os.getcwd(), 'Directory_Example', 'Directory_Example_02'){c}")
res = os.path.join(os.getcwd(), 'Directory_Example', 'Directory_Example_02')

print('\nres: ', res)

print(f'\n{b}os.chdir(res): {c}')
os.chdir(res)

print('\nos.getcwd(): ', os.getcwd())

print(f"""
{b}os.chdir('..')
os.chdir('..'){c}""")

os.chdir('..')
os.chdir('..')

print('\nos.getcwd(): ', os.getcwd())

# Listar os arquivos dentro do diretório
print(f'\n{a}Listar os arquivos dentro do diretório:{c}')

print(f'{b}\nos.listdir(): {c}')
print(os.listdir())

print('\nlen(os.listdir()): ', len(os.listdir()))

# Listar os arquivos dentro do diretório com mais detalhes
print(f'\n{a}Listar os arquivos dentro do diretório  com mais detalhes:{c}')

print(f'{b}\narquivos = list(os.scandir()) {c}')

scanner = os.scandir()
arquivos = list(scanner)

print(f"""{b}
scanner = os.scandir()
arquivos = list(scanner){c}
""")

print('arquivos: ', arquivos)

print('\narquivos[0]: ', arquivos[0])
print('arquivos[0].name: ', arquivos[0].name)
print('arquivos[0].inode: ', arquivos[0].inode())  # Identificador de inode
print('arquivos[0].is_dir: ', arquivos[0].is_dir())  #
print('arquivos[0].is_file: ', arquivos[0].is_file())
print('arquivos[0].is_symlink: ', arquivos[0].is_symlink())
print('arquivos[0].path: ', arquivos[0].path)
print('arquivos[0].stat: ', arquivos[0].stat())  # Estatísticas sobre o arquivo.

print(f'\n{b}scanner.close(){c}')
scanner.close()
