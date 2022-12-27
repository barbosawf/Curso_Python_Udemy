"""
Entendendo o *args

0 *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterísco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo.

O parâmetro *args utilzado numa função coloca os valores extras informados em uma tupla.
Lembrando que tuplas são imutáveis.
"""

# Exemplo 01
print("Exemplo 01")


def soma_todos_numeros(*args):
    return sum(args)


print("""
def soma_todos_numeros(*args):
    return sum(args)
    """)
print('soma_todos_numeros(): ', soma_todos_numeros())
print('soma_todos_numeros(1, 2, 3): ', soma_todos_numeros(1, 2, 3))
print('soma_todos_numeros(1, 2, 3, 4, 5): ', soma_todos_numeros(1, 2, 3, 4, 5))

# Exemplo 02
print("\nExemplo 02")


def soma_todos_numeros(nome, sobrenome, *args):
    lista = [nome, sobrenome, args]  # não dá certo da seguinte forma: list(nome, sobrenome, args)
    return lista


print("""
def soma_todos_numeros(nome, email, *args):
    return list(nome, email, sum(args))
    """)
print('soma_todos_numeros(): ', soma_todos_numeros('Agenlina', 'Jolie'))
print('soma_todos_numeros(1, 2, 3): ', soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3))
print('soma_todos_numeros(1, 2, 3, 4, 5): ', soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3, 4, 5))

# Exemplo 03
print("\nExemplo 03")


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é...'


print("""
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é...'
    """)
print('verifica_info(): ', verifica_info())
print("verifica_info(1, True, 'University', 'Geek'): ", verifica_info(1, True, 'University', 'Geek'))
print("verifica_info(1, 'University', 3.453): ", verifica_info(1, 'University', 3.453))


# Exemplo 03
print("\nExemplo 03")


def lista_num(*args):
    return args


print("""
def lista_num(*args):
    return args
    """)

print('lista_num([1, 2, 3], 4, 5): ', lista_num([1, 2, 3], 4, 5))


# Exemplo 04 - Uso de desempacotamento
print("\nExemplo 04")


def lista_num(*args):
    return sum(args)


print("""
def lista_num(*args):
    return args
    """)

print('lista_num(*[1, 2, 3], 5, 6): ', lista_num(*[1, 2, 3], 5, 6))

print('O asterisco na frente da lista desempacota a lista. Se não tiver dá erro.')

# Exemplo 05
print('\nExemplo 05')

lista = [2, 3, 5]
print('lista = [2, 3, 5]')
print('\nlista', lista)
print('*lista: ', *lista)
