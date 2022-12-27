"""
Documentando funções com Docstrings

OBS. Pode-se ter acesso a documentação de uma função em Python utilizando:
1 - help()
2 - __doc__
"""


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(help(diz_oi))

print('\ndiz_oi.__doc__: ', diz_oi.__doc__)


def exponecial(numero, potencia=2):
    """
    Uma função simples que retorna um número elevado a uma potência!
    :param numero: base que será elevada a uma determinada potência;
    :param potencia: Potência (default=2);
    :return: retorna o resultado do numero elevado a potencia.
    """
    return numero ** potencia


print('\nexponencial.__doc__: ', exponecial.__doc__)
