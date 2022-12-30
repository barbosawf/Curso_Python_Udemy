"""
Filter
filter(): serve para filtrar dados de uma certa coleção.

"""

import statistics

# Exemplo 01. Dados coletados de algum sensor.
print('Exemplo 01. Dados coletados de algum sensor.')

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print("""
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)
""")

print('media: ', media)

res1 = filter(lambda x: x > media, dados)
res2 = filter(lambda x: x > statistics.mean(dados), dados)

print("""
res1 = filter(lambda x: x > media, dados)
res2 = filter(lambda x: x > statistics.mean(dados), dados)
""")

print('list(res1): ', list(res1))
print('list(res2): ', list(res2))
print('list(res2): ', list(res2), 'Quando usa duas vezes fica vazio, pois fica na mémoria apenas na primeira vez.')

# Exemplo 02. Dados faltantes.
print('\nExemplo 02. Dados faltantes.')

paises = ['', 'Argentina', '', 'Brasil', 'Bélgica', 'Paraguai', 'Colômbia', '', 'Uruguai']
print('paises: ', paises)

res1 = filter(lambda x: len(x.strip()) > 0, paises)
res2 = filter(lambda x: x.strip() != '', paises)
res3 = filter(None, paises)

print("""
res1 = filter(lambda x: len(x.strip()) > 0, paises)
res2 = filter(lambda x: x.strip() != '', paises)
res3 = filter(None, paises)
""")

print('list(res1): ', list(res1))
print('list(res2): ', list(res2))
print('list(res3): ', list(res3))

# Exemplo 03. Filtrar os usuários que estão inativos no Tweeter
print('\nExemplo 03. Filtrar os usuários que estão inativos no Tweeter')

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Terminei de escovar os dentes']},
    {'username': 'gal', 'tweets': []},
    {'username': 'lisandra', 'tweets': ['Vou sair hoje', 'Acabei não saindo']},
]

print("""
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Terminei de escovar os dentes']},
    {'username': 'gal', 'tweets': []},
    {'username': 'lisandra', 'tweets': ['Vou sair hoje', 'Acabei não saindo']},
]
""")

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print("inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))")
print('inativos: ', inativos)

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print("\ninativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))")
print('inativos: ', inativos)

apenas_nomes = list(map(lambda x: x['username'], inativos))
print("\napenas_nomes = list(map(lambda x: x['username'], inativos))")
print('apenas_nomes: ', apenas_nomes)

# Exemplo 04. Filtrar os usuários que estão inativos no Tweeter (Combinação de filter e map)
print('\nExemplo 04. Filtrar os usuários que estão inativos no Tweeter (Combinação de filter e map)')


def filter_name(dicionario):
    usuario = list(filter(lambda u: not u['tweets'], dicionario))
    return list(map(lambda x: x['username'], usuario))


print("""
def filter_name(dicionario):
    usuario = list(filter(lambda u: not u['tweets'], dicionario))
    nomes = list(map(lambda x: x['username'], usuario))
    return nomes
    """)

print('filter_name(inativos): ', filter_name(inativos))

# Exemplo 05. Filtrar os usuários que estão inativos no Tweeter (Combinação de filter e map)
print('\nExemplo 05. Filtrar os usuários que estão inativos no Tweeter (Combinação de filter e map)')
nomes = list(map(lambda x: x['username'], filter(lambda u: not u['tweets'], inativos)))
print("nomes = list(map(lambda x: x['username'], filter(lambda u: not u['tweets'], inativos)))")
print('nomes: ', nomes)

# Exemplo 06. Criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres.
print("\nExemplo 06. Criar uma lista contendo 'Sua instrutura é' + nome,"
      "desde que cada nome tenha menos de 5 caracteres.")

nomes = ['Vanessa', 'Ana', 'Maria', 'Lorena', 'Rute', 'Ivana', 'Isabela', 'Laís']

lista = list(map(lambda nome: f'Sua instrutora é {nome}.', filter(lambda nome: len(nome) < 5, nomes)))
print('\nnomes: ', nomes)
print("lista = list(map(lambda nome: f'Sua instrutora é {nome}.', filter(lambda nome: len(nome) < 5, nomes)))")

print('lista: ', lista)
