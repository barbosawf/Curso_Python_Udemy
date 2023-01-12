"""
seek() é utilizado para movimentar o cursor pelo arquivo

OBS: Quando abrimos um arquivo com a funçao open() é criada uma conexão entre o arquivo no disco
do compotador e o programa. Essa conhexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos
fechar a conexão utilizando a função close().

Se tentarmos manipular o arquivo depois de fechado acontece um ValueError
"""
a = '\033[0;33m'
c = '\033[0;36m'
b = '\033[m'

arquivo = open('Texto_01.txt', encoding='utf-8')
print(arquivo.read())

# Movimentar o cursor pelo arquivo com a função seek()
print(f'\n{a}Movimentar o cursor pelo arquivo com a função seek(){b}')

print(f"""{c}
arquivo.seek(0)
print(arquivo.read()){b}
""")

arquivo.seek(0)
print(arquivo.read())

print(f"""{c}
arquivo.seek(22)
print(arquivo.read()){b}
""")

arquivo.seek(22)
print(arquivo.read())

# Fazer leitura linha a linha
print(f'\n{a}Fazer leitura linha a linha{b}')

print(f"""{c}
arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline()){b}
""")

arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())

linhas = arquivo.readlines()

# Usando o readLines
print(f'\n{a}Usando o readLines{b}')
arquivo.seek(0)

linhas = arquivo.readlines()
tipo = type(linhas)
tamanho = len(linhas)

print(f"""{c}
linhas = arquivo.readlines()
tipo = type(linhas)
tamanho = len(linhas){b}
""")

print('linhas:  ', linhas)
print('tipo:    ', tipo)
print('tamanho: ', tamanho)

# Abrindo, lendo e fechando o arquivo
print(f'\n{a}Abrindo, lendo e fechando o arquivo{b}')

print(f"""{c}
arquivo = open('Texto_01.txt', encoding=True)
ret = arquivo.read()
print(ret)
arquivo.close(){b}
""")

arquivo = open('Texto_01.txt', encoding='utf-8')
ret = arquivo.read()
print(ret)
arquivo.close()

print('arquivo.closed: ', arquivo.closed)

# Limintando a leitura de caracteres
print(f'\n{a}Limintando a leitura de caracteres{b}')

print(f"""{c}
arquivo = open('Texto_01.txt', encoding='utf-8')
ret = arquivo.read(50)
print(ret){b}
""")

arquivo = open('Texto_01.txt', encoding='utf-8')
ret = arquivo.read(50)
print(ret)