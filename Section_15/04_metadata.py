"""
Preservando metadatas com wraps

Metadados -> São dados intrínsicos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.
"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'


# Problema
print(f'\n{a} Problema{c}')


print(f'''{b}
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {{funcao.__name__}}.')
        print(f'Aqui a documentação: {{funcao.__doc__}}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b{c}
''')


def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {funcao.__name__}.')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print('ATENÇÃO! O problema ocorre porque a importação do nome e da documentação é da função logar, e não da soma.')
print('soma.__name__: ', soma.__name__)
print('soma.__doc__: ', soma.__doc__)


# Resolvendo o problema
print(f'\n{a}Resolvendo o problema{c}')


print(f'''{b}
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {{funcao.__name__}}.')
        print(f'Aqui a documentação: {{funcao.__doc__}}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b{c}
''')

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função {funcao.__name__}.')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print('ATENÇÃO! O problema foi resolvido usando o decorator wraps do pacote functools. Apenas isto resolve.')
print('soma.__name__: ', soma.__name__)
print('soma.__doc__: ', soma.__doc__)
