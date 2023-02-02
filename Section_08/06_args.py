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

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo 01
print(f"{a}Exemplo 01{c}")


def soma_todos_numeros(*args):
    return sum(args)


print(f"""{b}
def soma_todos_numeros(*args):
    return sum(args){c}
    """)

print('soma_todos_numeros(): ', soma_todos_numeros())
print('soma_todos_numeros(1, 2, 3): ', soma_todos_numeros(1, 2, 3))
print('soma_todos_numeros(1, 2, 3, 4, 5): ', soma_todos_numeros(1, 2, 3, 4, 5))

# Exemplo 02
print(f"{a}\nExemplo 02{c}")


def soma_todos_numeros(nome, sobrenome, *args):
    lista = [nome, sobrenome, args]  # não dá certo da seguinte forma: list(nome, sobrenome, args)
    return lista


print(f"""{b}
def soma_todos_numeros(nome, email, *args):
    return list(nome, email, sum(args)){c}
    """)

print("soma_todos_numeros('Agenlina', 'Jolie'): ", soma_todos_numeros('Agenlina', 'Jolie'))
print("soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3): ", soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3))
print("soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3, 4): ", soma_todos_numeros('Agenlina', 'Jolie', 1, 2, 3, 4))

# Exemplo 03
print(f"{a}\nExemplo 03{c}")


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é...'


print(f"""{b}
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é...'{c}
    """)

print('verifica_info(): ', verifica_info())
print("verifica_info(1, True, 'University', 'Geek'): ", verifica_info(1, True, 'University', 'Geek'))
print("verifica_info(1, 'University', 3.453): ", verifica_info(1, 'University', 3.453))


# Exemplo 04
print(f"{a}\nExemplo 04{c}")


def lista_num(*args):
    return args


print(f"""{b}
def lista_num(*args):
    return args{c}
    """)

print('lista_num([1, 2, 3], 4, 5): ', lista_num([1, 2, 3], 4, 5))


# Exemplo 05 - Uso de desempacotamento
print(f"{a}\nExemplo 05{c}")


def lista_num(*args):
    return sum(args)


print(f"""{b}
def lista_num(*args):
    return args{c}
    """)

print('lista_num(*[1, 2, 3], 5, 6): ', lista_num(*[1, 2, 3], 5, 6))

print('O asterisco na frente da lista desempacota a lista. Se não tiver dá erro.')

# Exemplo 06
print(f'{a}\nExemplo 06{c}')

lista = [2, 3, 5]
print('lista = [2, 3, 5]')
print('\nlista', lista)
print('*lista: ', *lista)
