"""
Módulos Externos (-m ensurepip --default-pip;  python -m ensurepip)

Utiliza-se o gerenciador de pacotes Python chamado Pip - Python Installer Package

Pacotes externos oficiais podem ser conhecidos em: https://pypi.org
"""


from colorama import init, Fore, Back


import colorama

print(dir(colorama))

init()

print(Fore.MAGENTA + 'Geek University')

print(Back.YELLOW + Fore.BLACK + 'Geek University')


# pandas, numpy, openxl
