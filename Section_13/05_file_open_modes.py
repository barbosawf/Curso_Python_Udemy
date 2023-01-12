"""
Modos de abertura de arquivo
r -> abre para leitura
w -> abre para escrita - sobrescreve caso o arquivo já exista
x -> abre para escrita somente se o arquivo não existir
a -> se o arquivo não existir será criado. Mas se existir, adiciona o conteúdo ao final do arquivo existente.
+ -> abre para o modo de atualização: leitura e escrita.
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'


# Exemplo 01 de escrita - modo 'x' (abre para escrita somente se o arquivo não existir)
print(f"\n{a}Exemplo 01 de escrita - modo 'x' (abre para escrita somente se o arquivo não existir){c}")

try:
    with open('university.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo\n')
except FileExistsError as er:
    print(f'O arquivo já existe: {er}.')


# Exemplo 02 de escrita - modo 'a' (adiciona informação ao arquivo já existente, não substitui)
print(f"\n{a}Exemplo 02 de escrita - modo 'a' (adiciona informação ao arquivo já existente, não substitui){c}")

with open('frutas.txt', 'a+', encoding='utf-8') as arquivo:
    while True:
        fruta = str(input('Informe uma fruta ou sair para sair: ')).lower().strip()
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
