"""
Forçando tipos de dados com decoradores

zip - O que o zip faz:

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)

(1, 2), (3, 4), (5, 6)

"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'


def forca_tipo(*tipos):
    def decorador(funcao):
        def convert(*args, **kwargs):
            novo_args = []
            for valor, tipo in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return convert
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


repete_msg(1232, '3')
repete_msg('Geek', '3')

dividir('1', 5)
dividir('5', '2')

