"""
Levantando os próprios erros com raise.

raise -> Lança exceções. É uma palavra reservada.

raise é útil para criar nossas próprias execeções e mensagen de erro.

OBS. O raise assim como o return finaliza a função.
"""

# raise ValueError('Valor incorreto')


# Exemplo 01
print('Exemplo 01')


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'cor precisa ser qualquer uma das seguintes: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')

# colore('Geek', 23)
# colore(True, 'azul')
# colore('Geek', 'violeta')

