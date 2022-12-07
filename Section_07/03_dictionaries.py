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
print("paises.get('br'): ", paises.get('br'))
print("paises.get('ru'): ", paises.get('ru'))


