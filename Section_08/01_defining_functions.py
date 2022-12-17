"""
Definindo Funções

— Funções são pequenos trechos de códigos que realizam tarefas especídficas;
— Pode ou não receber entradas de dados e retornar uma saída de dados;
— Muito úteis para procedimentos similares por repetidas vezes;

Princípio:
- DRY - Don't repeat yourself (Não repita você mesmo / Não repita seu código)

OBS.: Se uma função for escrita para realizar várias tarefas é apreciável simplificar a função.
"""

# Exemplo de utilização de funções
print('Exemplo de utilização de funções')
cores = ['verde', 'amarelo', 'azul', 'branco']
print("cores = ['verde', 'amarelo', 'azul', 'branco']")

curso = 'Programação em Python: Essencial'
print("\ncurso = 'Programação em Python: Essencial'")

# Uso de uma função integrada do python (Build-in)
print('\nUso de uma função integrada do python (Build-in)')

print('print(cores):', cores)

print('\nprint(curso):', curso)

# Função que recebe dados de entrada
print('\nFunção que recebe dados de entrada')
cores.append('roxo')
print("cores.append('roxo')")
print("cores ", cores)

# Função que não recebe nenhum dado de entrada
print('\nFunção que não recebe nenhum dado de entrada')
cores.clear()
print('cores.clear()')
print("cores: ", cores)

# Definição de funções
"""
Definição de funções

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função
    
nome_da_função -> Sempre com letras minúsculas e se for composto separado por underline (snake case)
parâmetros_de_entrada -> Opcionais e se mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função -> Chamado de corpo da função ou implementação. É onde o processamento da função ocorre.
No bloco, pode-se ter ou não retorno da função.

OBS. A palavra que define a função em Python é def.
Abre-se o bloco de código com dois pontos (:).
"""

# Primeira função:
print('\nPrimeira função:')


def diz_oi():
    print('Oi!')


print("""
def diz_oi():
    print('Oi!')
""")

print("diz_oi(): ")
diz_oi()

# Segunda função:
print('\nSegunda função:')


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


print("""
def cantar_parabéns():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
""")

print("cantar_parabens(): ")
cantar_parabens()

# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável
print('\nEm Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável')

canta = cantar_parabens
print("canta = cantar_parabens")

print('canta(): ')
canta()
