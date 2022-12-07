"""
Dicionários:

OBS.: Em algumas linguagens de programação, os dicionários são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Sobre dicionários:
    - Chave e valor são separados por dois pontos, ou seja, chave:valor;
    - Tanto a chave quanto o valor pordem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


"""
# Criação de dicionários
print('Criação de dicionários')

# Forma 01
print('\nForma 01')

# Dicionários são representados por chaves {}.
print('\nDicionários são representados por chaves {}.')
d = {}
print('d:       ', d)
print('type(d): ', type(d))

print(' ')
print("paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}")
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('paises:       ', paises)
print('type(paises): ', type(paises))

# Forma 02
print('\nForma 01')
print("paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')")
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print('paises: ', paises)

# Acesso de elementos nos dicionários:
print('\nAcesso de elementos nos dicionários: através das chaves.')
print("paises['br']: ", paises['br'])
print("paises['py']: ", paises['py'])

# Se colocar uma chave que não existe dá erro:
print('\nSe colocar uma chave que não existe dá erro:')
print("paises['ru'])")

# Mas se acessar através do comando get(), não dá erro:
print('\nMas se acessar através do comando get(), não dá erro:')
print("paises.get('br'):                   ", paises.get('br'))
print("paises.get('ru'):                   ", paises.get('ru'))
print("paises.get('ru', 'Não encontrei!'): ", paises.get('ru', 'Não encontrei!'))
print("paises.get('py', 'Não encontrei!'): ", paises.get('py', 'Não encontrei!'))

# Verificar a presença de uma determinada chave numa tupla:
print('\nVerificar a presença de uma determinada chave numa tupla:'
      'Busca por chave, não por valor')
print("'br' in paises: ", 'br' in paises)
print("'ru' in paises: ", 'ru' in paises)

# Podemos utilizar qualquer tipo de dado numa tupla (int, float, string, boolean, lista, tupla, dicionário):
print('\nPodemos utilizar qualquer tipo de dado numa tupla (int, float, string, boolean, lista, tupla, dicionário):')

# Tuplas podem ser utilizadas como chaves de dicionários:
print('\nExemplo: Tuplas podem ser utilizadas como chaves de dicionários:')
localidades = {
      (35.6895, 39.6917): 'Escritório em Tókio',
      (40.7128, 74.0060): 'Escritório em Nova Iorque',
      (37.7749, 122.4194): 'Escritório em São Paulo',
}
print('localidades:', localidades)
print('type(localidades):', type(localidades))

# Adicionar elementos num dicionário:
print('\nAdicionar elementos num dicionário:')

receita = dict(jan=100, fev=120, mar=90, abr=130)
print('receita:       ', receita)
print('type(receita): ', type(receita))

# Forma 01
print('\nForma 01')
receita['mai'] = 300
print("receita['mai'] = 300")
print('receita:       ', receita)

# Forma 02
print('\nForma 02')
novo_dado = {'jun': 422}
print("novo_dados = {'jun': 422}")
receita.update(novo_dado)
print("receita.update(novo_dado)")
print('receita:    ', receita)

# Atualizar dados num dicionário:
print('\nAtualizar dados em um dicionário:')

# Forma 01
print('\nForma 01')
receita['jun'] = 550
print("receita['jun'] = 550")
print('receita: ', receita)

# Forma 02
print('\nForma 02')
receita.update({'jun': 600})
print("receita.update({'jun': 600}) ")
print('receita: ', receita)

# CONCLUSÃO 01: A forma de adicionar ou atualizar elementos num dicionário é a mesma.
# CONCLUSÃO 02: Em dicionários não se pode ter chaves repetidas.

print("""
# CONCLUSÃO 01: A forma de adicionar ou atualizar elementos num dicionário é a mesma.
# CONCLUSÃO 02: Em dicionários não se pode ter chaves repetidas.
""")

# Remover dados de um dicionário:
print('\nRemover dados de um dicionário:')

# Forma 01 (utilizando a função pop())
print('\nForma 01 (utilizando a função pop()')
receita = dict(jan=100, fev=120, mar=90)
print('receita: ', receita)
receita.pop('mar')  # Precisa sem informar a chave
print("receita.pop('mar')")
print('receita: ', receita)

# OBS.: Ao remover um elemento, o valor do elemento é sempre retornado.
print('\nAo remover um elemento, o valor do elemento é sempre retornado.')
receita = dict(jan=100, fev=120, mar=90)
print('receita:            ', receita)
print("receita.pop('mar'): ", receita.pop('mar'))

# Forma 02 (utilizando o comando del)
print('\nForma 02 (utilizando o comando del). Neste caso o valor removido não é reornado.')
receita = dict(jan=100, fev=120, mar=90)
print('receita:            ', receita)
del receita['fev']
print("del receita['fev']")
print('receita:            ', receita)

# OBS.: Se a chave não existir será mostrado um KeyError
print('\n# OBS.: Se a chave não existir será mostrado um KeyError')

# Imagine que você tenha um comércio eletrônico com um carrinho de compras em que se possa adicionar produtos.

"""
Carrinho de Compras:
      Produto 1:
            - nome;
            - quantidade;
            - preço.
      Produto 2:
            - nome;
            - quantidade;
            - preço.

"""
# 1 — Podemos utilizar uma lista para isso:
print('\n1 — Podemos utilizar uma lista para isso:')
print("""
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
""")
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# 2 — Podemos utilizar uma tupla para isso:
print('\n2 — Podemos utilizar uma tupla para isso:')

print("""
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)
""")
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# 3 — Podemos utilizar um dicionário para isso:
print('\n3 — Podemos utilizar um dicionário para isso:')

print("""
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
""")
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos para dicionários:
print('\nMétodos para dicionários:')

d = dict(a=1, b=2, c=3)
print('d:       ', d)
print('type(d): ', type(d))

# Limpar o dicionário (zerar dados)
print('\nLimpar o dicionário (zerar dados):')
print('d:       ', d)
d.clear()
print('d.clear()')
print('d:       ', d)

# Copiar um dicionário para outro com a função copy(). Deep copy:
print('\nCopiar um dicionário para outro:')
d = dict(a=1, b=2, c=3)
print('d:       ', d)
novo = d.copy()
print('novo = d.copy()')
print('novo:    ', novo)

# Atualizar o dicionário copiado com a função copy():
print('\nAtualizar o dicionário copiado com a função copy()')
print('d:       ', d)
novo['d'] = 4
print("novo['d'] = 4")
print('d:       ', d)
print('novo:    ', novo)

# Copiar um dicionário utilizando o sinal de atribuição '='. Shallow copy:
print("\nCopiar um dicionário utilizando o sinal de atribuição '='. Shallow copy:")
novo = d
print('novo = d')
print('d:       ', d)
print('novo:    ', novo)

# Atualizar o dicionário copiado com o sinal de atribuição '=':
print("\nAtualizar o dicionário copiado com o sinal de atribuição '=':")
print('d:       ', d)
novo['d'] = 4
print("novo['d'] = 4")
print('d:       ', d)
print('novo:    ', novo)

# Forma não usual de criação de dicionários utilizando a função fromkeys:
print('\nForma não usual de criação de dicionários a função fromkeys:')
outro = {}.fromkeys('a', 'b')
print("outro = {}.fromkeys('a', 'b')")
print('outro: ', outro)

# Com a função fromkeys, o primeiro argumento pode ser iterável e o segundo um valor único:
print('\nCom a função fromkeys, o primeiro argumento pode ser iterável e o segundo um valor único:')
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print("\nusuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')")
print('usuario: ', usuario)

print("\nveja = {}.fromkeys('teste', 'valor')")
veja = {}.fromkeys('teste', 'valor')
print('veja: ', veja)
print("OBS: Não repete o 't' e o 'e', pois em dicionários não há repetição de chaves")

print("\nveja = {}.fromkeys(range(5), 'valor')")
veja = {}.fromkeys(range(5), 'valor')
print('veja: ', veja)

