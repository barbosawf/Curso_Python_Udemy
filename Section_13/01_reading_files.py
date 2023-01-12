"""
LEMBRAR: https://stackoverflow.com/questions/33589145/pycharm-55-utf-8-encoding
Leitura de aquivos
Para ler o conteúdeo de um arquivo em Python, utilizamos a função integada open().

open() -> Na forma mais simples de utilização apenas um parâmetro de entrada é passado (caminho do arquivo a ser lido).
Essa função retorna um _io. TextIOWrapper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
FileNotFoundError.

A função read() lê o conteúdo inteiro do arquivo.

"""
a = '\n\033[0;33m'
b = '\033[m'

# Exemplo
print(f'{a}Exemplo{b}')
arquivo = open('Texto_01.txt', encoding='utf-8')

print('\narquivo: ', arquivo)

print('\ntype(arquivo): ', type(arquivo))


# Para ler o conteúdo de um arquivo após sua abertura devemos utilizar a função read()

print(f'{a}Para ler o conteúdo de um arquivo após sua abertura devemos utilizar a função read(){b}')

ret = arquivo.read()
print("\nf'{ret}': ", f'\n{ret}')

print('\ntype(ret): ', type(ret))

print("\nret.split('barra_n'): ")
print(ret.split('\n'))

