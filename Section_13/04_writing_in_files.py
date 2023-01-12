"""
Escrevendo em arquivos

OBS. Ao abrir um arquivo para leitura não podemos realizar a escrita. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

O argumento da função write() precisa ser ‘string’.

Se o arquivo não existir será criado, mas sele já existir, o anterior será apagado e um novo será criado.
Dessa forma, o inteiro conteúdo no arquivo anterior é perdido.

"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo 01 de escrita - modo 'w' (write)
print(f"{a}Exemplo de escrita - modo 'w' (write){c}")

print(f"""{b}
with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil!\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.'){c}
""")

with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil!\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

arquivo = open('novo.txt', encoding='utf-8')
print(arquivo.read())
arquivo.close()

# Exemplo 02 de escrita - modo 'w' (write)
print(f"\n{a}Exemplo 02 de escrita - modo 'w' (write){c}")

print(f"""{b}
arquivo2 = open('mais_novo.txt', 'w', encoding='utf-8')
arquivo2.write('Um texto qualquer!\n')
arquivo2.write('Mais uma linha adicionada.\n')
arquivo2.write('Esta é a última linha, finalmente.')

arquivo2 = open('mais_novo.txt', encoding='utf-8')
print(arquivo2.read())
arquivo2.close(){c}
""")

arquivo2 = open('mais_novo.txt', 'w', encoding='utf-8')
arquivo2.write('Um texto qualquer!\n')
arquivo2.write('Mais uma linha adicionada.\n')
arquivo2.write('Esta é a última linha, finalmente.')

arquivo2 = open('mais_novo.txt', encoding='utf-8')
print(arquivo2.read())
arquivo2.close()

# Exemplo 03 de escrita - modo 'w' (write)
print(f"\n{a}Exemplo 03 de escrita - modo 'w' (write){c}")

print(f"""{b}
with open('mais_novo_ainda.txt', 'w', encoding='utf-8') as arquivo3:
    arquivo3.write('Geek\n' * 5)
    
arquivo3 = open('mais_novo.txt', encoding='utf-8')
print(arquivo3.read())
arquivo3.close(){c}
""")

with open('mais_novo_ainda.txt', 'w', encoding='utf-8') as arquivo3:
    arquivo3.write('Geek\n' * 5)

arquivo3 = open('mais_novo_ainda.txt', encoding='utf-8')
print(arquivo3.read())
arquivo3.close()

# Exemplo 04 de escrita - modo 'w' (write)
print(f"\n{a}Exemplo 04 de escrita - modo 'w' (write){c}")

with open('user_data.txt', 'w', encoding='utf-8') as arquivo4:
    for i in range(5):
        arquivo4.write(str(input(f'Escreva a linha {i + 1}: ')))
        arquivo4.write('\n')


# Exemplo 05 de escrita - modo 'w' (write)
print(f"\n{a}Exemplo 05 de escrita - modo 'w' (write){c}")

with open('frutas.txt', 'w', encoding='utf-8') as arquivo5:
    while True:
        fruta = str(input(f'Informe a fruta ou digite sair: '))
        if fruta != 'sair':
            arquivo5.write(fruta + '\n')
        else:
            break
