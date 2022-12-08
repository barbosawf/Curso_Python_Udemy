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
print("set([1, 2, 3, 3, 1, 5]): ", set([1, 2, 3, 3, 1, 5]))
print("set((1, 2, 3, 3, 1, 5)): ", set((1, 2, 3, 3, 1, 5)))

# Forma 02:
print('\nForma 02')

s = set({1, 2, 3, 3, 1, 5})
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

lista = [99, 2, 34, 23, 12, 44, 5, 2, 1]
tupla = tuple(lista)
dicionario = dict(lista)
conjunto = set(lista)

print('lista', lista)
print('tupla', tupla)
print('dicionário', dicionario)
print('conjunto', conjunto)

