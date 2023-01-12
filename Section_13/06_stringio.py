"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    — Permissão de Leitura → para ler o arquivo
    — Permissão de Escrita → para escrever o arquivo

É utilizado ára ler e criar arquivos em memória.
Podemos criar um arquivo em memória já com uma 'string' ou mesmo vazio para inserirmos texto depois
"""
a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Utilização do StringIO
print(f'{a}Utilização do StringIO{c}')

print(f"""{b}
from io import StringIO

msg = 'Esta é apenas uma string normal'
arquivo = StringIO(msg){c}
""")

from io import StringIO

msg = 'Esta é apenas uma string normal'
arquivo = StringIO(msg)
print('arquivo.read(): ', arquivo.read())

print(f"""{b}
arquivo.write('barra_n' + 'Outro texto')
arquivo.seek(0){c}
""")

arquivo.write('\n' + 'Outro texto')
arquivo.seek(0)

print('arquivo.read(): ')
print(arquivo.read())
