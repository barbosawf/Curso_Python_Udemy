"""
Funções com Parâmetro Padrão (Default Parameters)
- Funções em que a passagem de parâmetro é opcional;

# Exemplo de função em que a passagem de parâmetro é opcional:
print('Geek University')

print()
"""

# Exemplo 01
print('Exemplo 01')


def quadrado(n=2):
    return n ** 2


print("""
def quadrado(n=2):
    return n ** 2
""")

print('quadrado(): ', quadrado())

# Exemplo 02
print('\nExemplo 02')


def exponencial(n=2, potencia=3):
    return n ** potencia


print("""
def exponencial(n=2, potencia=3):
    return n ** potencia
""")

print('exponencial(): ', exponencial())

# Exemplo 03
print('\nExemplo 03')


def exponencial(n, potencia=2):
    return n ** potencia


print("""
def exponencial(n, potencia=3):
    return n ** potencia
""")

print('exponencial(3): ', exponencial(3))

# Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# Exemplo de Erro!

print(
    """
# Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.
# Exemplo de Erro!
"""
)

print("""
def test(num=2, potencia):
    return num ** potencia
""")

print('potencia que está no final não é default. Isso dá erro se declarar um argumento.')

# Funções como parâmetro
print('\nFunções como parâmetro:')


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print("""
print('\nFunções como parâmetro:')


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)
""")

print('mat(5, 2): ', mat(5, 2))
print('mat(5, 2, subtracao): ', mat(5, 2, subtracao))
print('mat(5, 2, fun=subtracao): ', mat(5, 2, fun=subtracao))

# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais

print("""
Escopo - Evitar problemas e confusões

Variáveis globais e locais
""")

instrutor = 'Geek'


def diz_oi():
    return f'Oi, {instrutor}!'


print("""
instrutor = 'Geek'


def diz_oi():
    return f'Oi, {instrutor}!'
""")
print('diz_oi(): ', diz_oi())

nome = 'Geek'


def diz_oi():
    nome = "Python"  # Variável local
    return f'Oi, {nome}!'


print("""
nome = 'Geek'


def diz_oi():
    nome = "Python" # Variável local tem preferência
    return f'Oi, {nome}!'
""")
print('diz_oi(): ', diz_oi())

# Exemplo de erro
print('\nExemplo de erro:')

print(
    """
total = 0


def incrementa():
    total = total + 1 # UnboundLocalError (Variável local está sendo utilizada para processamento sem ter sido 
    # inicializada 
    return total
"""
)

# Exemplo que não dá erro

print('\nExemplo que não dá erro:')

print("""
total = 0


def incrementa():
    global total
    total = total + 1 # UnboundLocalError (Variável local está sendo utilizada para processamento sem ter sido 
    # inicializada 
    return total
""")

total = 0


def incrementa():
    global total
    total = total + 1
    return total


print('incrementa(): ', incrementa())
print('incrementa(): ', incrementa())
print('incrementa(): ', incrementa())

# Funções podem ser declaradas dentro de funções e têm uma forma especial de escopo de variáveis
print('\nFunções podem ser declaradas dentro de funções e têm uma forma especial de escopo de variáveis:')


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print("""
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
""")

print('fora(): ', fora())
print('fora(): ', fora())
print('fora(): ', fora())

print('dentro(): ', 'Dá erro, pois está dentro do escopo da função fora.')
