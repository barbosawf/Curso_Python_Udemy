"""
Módulo é apenas um arquivo Python que pode ter diversar funções para utilizarmos;

Pacote é um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado
para manter compatibilidade.

"""

import colorama as clm
clm.init()
a = '\033[0;33'
b = '\033[0;30;0m'
from Geek import Geek_01, Geek_02

print(clm.Fore.YELLOW + 'from Geek import Geek_01', b)

print('dir(Geek_01): ', dir(Geek_01))

print('\nGeek_01.pi: ', Geek_01.pi)

print('\nGeek_01.funcao1(3, 5): ', Geek_01.funcao1(3, 5))

print('\nGeek_02.curso: ', Geek_02.curso)

print('\nGeek_02.funcao2: ', Geek_02.funcao2())


from Geek.University import Geek_03, Geek_04


print(clm.Fore.YELLOW + '\nfrom Geek.University import Geek_03, Geek_04', b)

print('Geek_03.funcao3(): ', Geek_03.funcao3())

print('\nGeek_04.funca4(): ', Geek_04.funcao4())


from Geek.Geek_01 import funcao1


print(clm.Fore.YELLOW + '\nfrom Geek.Geek_01 import funcao1', b)


print('funcao1(5, 7): ', funcao1(5, 7))


from Geek.University.Geek_04 import funcao4


print(clm.Fore.YELLOW + '\nfrom Geek.University.Geek_04 import funcao4', b)


print('funcao4(): ', funcao4())
