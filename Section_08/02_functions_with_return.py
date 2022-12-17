"""
OBS.: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

A palavra return é que faz a função retornar o valor
"""

# Função sem retorno
print('Função sem retorno')


def quadrado_de_7():
    print(7 * 7)


print("\n"
      "def quadrado_de_7():\n"
      "    print(7 * 7)\n")

ret = quadrado_de_7()
print('\nret = quadrado_de_7()')
print('quadrado_de_7():', quadrado_de_7())
print('ret: ', ret)

# Função com retorno
print('\nFunção com retorno')


def quadrado_de_7():
    return 7 * 7


print("""
def quadrado_de_7():
    return 7 * 7
""")

ret = quadrado_de_7()
print('ret = quadrado_de_7()')
print('quadrado_de_7():', quadrado_de_7())
print('ret: ', ret)
print('quadrado_de_7() + 1:', quadrado_de_7() + 1)

"""
OBS.: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter fiferentes returns em uma função;
3 - Podemos retornar qualquer tipo de dado e até mesmo múltiplos valores em uma função.
"""
