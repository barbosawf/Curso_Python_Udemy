"""
Conjuntos
— Faz referência à Teoria dos Conjuntos da Matemática em qualquer linguagem.

— 'Sets' (conjuntos) não possuem valores duplicados;
— 'Sets' (conjuntos) não possuem valores ordenados;
— Elementos não são acessados via índice, ou seja, eles não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas
não nos importamos com a ordenação dels. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos ('sets') são referenciados em Python com chaves {}

Diferença entre conjuntos e mapas em Python
— Um dicionário tem chave/valor;
— Um conjunto tem apenas valor;
"""

# Definindo um conjunto?
print('Definindo um conjunto:')

# Forma 01:
print('\nForma 01:')
print('s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})')
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print('s:       ', s)
print('type(s): ', type(s))

print("""
OBS.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
      será ignorado sem gerar erro e não fará parte do conjunto.
""")

# Conversão de 'string', listas e tuplas para conjunto:
print('Conversão de string, listas e tuplas para conjunto:')
print("set('Geek University')): ", set('Geek University'))
print("{1, 2, 3, 3, 1, 5}: ", {1, 2, 3, 3, 1, 5})
print("{1, 2, 3, 3, 1, 5}: ", {1, 2, 3, 3, 1, 5})

# Forma 02:
print('\nForma 02')

s = {1, 2, 3, 3, 1, 5}
print('s:       ', s)
print('type(s): ', type(s))

print("""
if 3 in s:
    print('Tem o 3!')
else:
    print('Não tem o 3!')
""")
if 3 in s:
    print('Tem o 3!')
else:
    print('Não tem o 3!')

# Importante lembrar que, além de não termos valores ducplicados, não temos ordem:
print('\nImportante lembrar que, além de não termos valores ducplicados, não temos ordem:')

lista = [99, 2, 34, 23, 12, 44, 5, 2, 1, 34]
tupla = tuple(lista)
dicionario = {}.fromkeys(lista, None)
conjunto = set(lista)

print('lista:             ', lista)
print('tupla:             ', tupla)
print('dicionário.keys(): ', dicionario.keys())
print('conjunto:          ', conjunto)

# Podemos colocar qualquer categoria de dado em conjuntos (menos listas, conjuntos e booleanos):
print('\nPodemos colocar qualquer tipo de dado em conjuntos:')
s = {1, 'b', True, 34.33, 44}
print('s: ', s)

# Podemos iterar um conjunto:
print('Podemos iterar um conjunto:')
print('s: ', s)

print("""
for i in s:
    print(i)
""")

for i in s:
    print(i)

# Usos interessantes com sets
print('\nUsos interessantes com sets')
print("""
Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os 
visitantes informam manualmente a cidade de onde vieram.

Nós adicionamos cada cidade em uma lista Pythom, já que em uma lista podemos adicionar 
novos elementos e ter repetição.
""")

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print('Cidades: ', cidades)
print('Quantidade de pessoas: ', 'len(cidades): ', len(cidades))
print('Cidades diferentes: ', 'len(set(cidades)): ', len(set(cidades)))

# Adicionar elementos num conjunto:
print('\nAdicionar elementos num conjunto:')
s = {1, 2, 3}
print('s: ', s)
s.add(4)
print('s.add(4)')
print('s: ', s)
print('s.add(4)')
print('s: ', s, 'Duplicidade não gera erro, mas o novo elemento é ignorado.')

# Remover elementos num conjunto:
print('\nRemover elementos num conjunto:')
# Forma 01
print('\nForma 01')
s = {1, 2, 3}
print('s: ', s)
s.remove(2)
print('s.remove(2)')
print('s: ', s)

# Forma 02
print('\nForma 02')
s = {1, 2, 3}
print('s: ', s)
s.discard(2)
print('s.discard(2)')
print('s: ', s)
s.discard(33)
print('s.discard(33)')
print('s: ', s, 'O comando discard() não gera erro.')

# Copiar um conjunto para outro:
print('\nCopiar um conjunto para outro:')
s = {1, 2, 3}
print('s:    ', s)

# Forma 01 (Deep Copy)
print('\n# Forma 01 (Deep Copy)')
novo = s.copy()
print('novo = s.copy()')
print('novo: ', novo)
novo.add(4)
print('novo.add(4)')
print('novo: ', novo)
print('s:    ', s)

# Forma 02 (Shallow Copy)
print('\n# Forma 02 (Shallow Copy)')
novo = s
print('novo = s')
print('novo: ', novo)
novo.add(4)
print('novo.add(4)')
print('novo: ', novo)
print('s:    ', s)

# Remover todos os elementos de um conjunto:
print('\nRemover todos os elementos de um conjunto:')
s = {1, 2, 3}
print('s:       ', s)
s.clear()
print('s.clear()')
print('s:       ', s)

# Métodos Matemáticos de Conjuntos
print('\n# Métodos Matemáticos de Conjuntos')
print("""
Imagine que tenhamos dois conjuntos:
1) Um contendo estudantes do curso de Python
2) Outro contendo estudantes do curso de Java.
""")

est_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Mateus', 'Leonardo'}
est_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Pedro'}

print(est_python)
print(est_java)

# Alguns alunos que estudam Python também estudam Java
print('Alguns alunos que estudam Python também estudam Java')

# Gerar um conjunto de elementos únicos entre os dois conjuntos
print('\nGerar um conjunto de elementos únicos entre os dois conjuntos')

# Forma 01 - comando union()
print('\nForma 01 - comando union()')
unicos1 = est_python.union(est_java)
print('unicos1 = est_python.union(est_java)')
print('unicos1: ', unicos1)
print('')
unicos1 = est_java.union(est_python)
print('unicos1 = est_java.union(est_python)')
print('unicos1: ', unicos1)

# Forma 02 — comando pipe |
print('\nForma 02 - comando pipe |')
unicos2 = est_python | est_java
print('unicos2 = est_python | est_java')
print('unicos2: ', unicos2)

# Gerar um conjunto de elementos que estão em ambos os conjuntos:
print('\nGerar um conjunto de elementos que estão em ambos os conjuntos:')

# Forma 01 — comando intersection()
print('\nForma 01 - comando intersection()')
inter1 = est_python.intersection(est_java)
print('inter1 = est_python.intersection(est_java)')
print('inter1: ', inter1)
print('')
inter1 = est_java.intersection(est_python)
print('inter1 = est_java.intersection(est_python)')
print('inter1: ', inter1)

# Forma 02 - comando &
print('\nForma 02 - comando &')
inter2 = est_python & est_java
print('inter2 = est_python & est_java')
print('inter2: ', inter2)

# Gerar um conjunto de elementos que não estão no outro conjunto
print('\nGerar um conjunto de elementos que não estão no outro conjunto')
only_python = est_python.difference(est_java)
print('only_python = est_python.difference(est_java)')
print('only_python: ', only_python)

print('')
only_java = est_java.difference(est_python)
print('only_java = only_java.difference(est_python)')
print('only_java: ', only_java)

# Soma, maior, menor, tamanho:
print('\nSoma, maior, menor, tamanho:')
s = {4, 23, 7, 8, 34, 2}
print('s: ', s)
print('sum(s)', sum(s))
print('max(s)', max(s))
print('min(s)', min(s))
print('len(s)', len(s))
