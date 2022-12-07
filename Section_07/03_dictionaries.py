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
