"""
Try / Except / Else / Finally

Dica de quando e onse tratar código:

TODA ENTRADA DEVE SER TRATADA!

else é executado somente se o erro não ocorrer;
"""

# Exemplo 01 (else)
print('Exemplo 01 (else)')

print("""
try:
    num = int(input('Informe um número: '))
except ValueError as err:
    print(f'Ocorreu um ValueError: {err}')
else:
    print(f'Você digitou {num}')
    """)

try:
    num = int(input('Informe um número: '))
except ValueError as err:
    print(f'Ocorreu um ValueError: {err}')
else:
    print(f'Você digitou {num}')


# Exemplo 02 (finally)
print('\nExemplo 02 (finally)')

print("""
try:
    num = int(input('Informe um número: '))
except ValueError as err:
    print(f'Ocorreu um ValueError: {err}')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')  # O bloco finally sem é executado. Independente se houve exceção ou não.
    """)

try:
    num = int(input('Informe um número: '))
except ValueError as err:
    print(f'Ocorreu um ValueError: {err}')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')  # O bloco finally sem é executado. Independente se houve exceção ou não.


# Exemplo 03 (Forma ruim de tratar os erros)
print('\nExemplo 03 (Forma ruim de tratar os erros)')


def dividir(a, b):
    return a / b


try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print('O valor precisa ser numérico.')

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico.')

try:
    print('dividir(num1, num2): ', dividir(num1, num2))
except NameError:
    print('Ocorreu um NameError')


# Exemplo 04 (Forma correta de tratar os erros)
print('\nExemplo 04 (Forma correta de tratar os erros)')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto.'
    except NameError:
        return 'Ocorreu um NameError'
    except ZeroDivisionError:
        return 'Não há divisão por zero.'


print("""
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto.'
    except NameError:
        return 'Ocorreu um NameError'
    except ZeroDivisionError:
        return 'Não há divisão por zero.'
        """)

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplo 05 (Forma correta de tratar os erros: tratamento semi-genérico)
print('\nExemplo 05 (Forma correta de tratar os erros: tratamento semi-genérico)')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Ocorreu um problema: {erro}'


print("""
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema!'
        """)

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
