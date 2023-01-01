"""
PDB -> Python Debugger

Bug -> Inseto

"""

# Exemplo 01. Debugando com o PyCharm
print('# Exemplo 01. Debugando com o PyCharm')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Ocorreu um problema: {erro}'


print(dividir(4, 3))

# Exemplo 02. Python Debugger (deve-se importar a biblioteca pdb e, então, utilizar a função set_trace())
print('\nExemplo 02. Python Debugger (deve-se importar a biblioteca pdb e, então, utilizar a função set_trace())')

print("""Comandos básicos do pdb:
l: lista onde estamos no código
n: próxima lina
p: imprime variável
c continua a execução - finaliza o debugging""")

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 03. Python Debugger (deve-se importar a biblioteca pdb e, então, utilizar a função set_trace())
print('\nExemplo 03. Python Debugger (deve-se importar a biblioteca pdb e, então, utilizar a função set_trace())')
print('Import pdb no meio do código é mais comum, pois a debugação é feita durante o desenvolvimento.')

print("""Comandos básicos do pdb:
l: lista onde estamos no código
n: próxima lina
p: imprime variável
c continua a execução - finaliza o debugging""")

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 4. A partir do Pytho 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug
# foi imporporada como função built-in (integrada) chmada breakpoint()

print("""
Exemplo 4. A partir do Pytho 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug
           foi imporporado como função built-in (integrada) e é chamado de breakpoint()
""")

print("""Comandos básicos do pdb:
l: lista onde estamos no código
n: próxima lina
p: imprime variável
c continua a execução - finaliza o debugging""")

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo 05 Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
print('\nExemplo 05 Cuidado com conflitos entre nomes de variáveis e os comandos do pdb')

print("""Para chamar os valores das variáveis, deve-se colocar o comando p do breakpoint()
         e em seguida o nome da variável""")


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 4, 7))
