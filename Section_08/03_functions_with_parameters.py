"""
Funções com parâmetros
- Funções que recebem parâmetros para serem processados dentro da mesma;

Há funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

OBS.: Não se pode colocar parâmetros a mais ou a menos quando o parâmetro for obrigatório

Diferença entre parâmetros e argumentos
- Parâmetros são variáveis declaradas na definição de uma função;
- Argumentos são dados passados durante a execução de uma função;

A ordem dos parâmetros importa caso eles não sejam informados, mas se a entrada dos argumentos
for feita com a declaração dos parâmetros, não importa a ordem.
"""

# Exemplo 01
print('Exemplo 01')


def quadrado(n):
    return n * n


print("""
def quadrado(n):
    return n * n
""")

print('quadrado(7): ', quadrado(7))
print('quadrado(2): ', quadrado(2))

# Exemplo 02
print('\nExemplo 02')


def cantar_parabens(aniversariante):
    return \
        f"""\nParabéns pra você,
Nesta data querida,
Muitas felicidades,
Muitos anos de vida,
Viva, {aniversariante}!
 """


print("""
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva, {aniversariante}')
""")

print('cantar_parabens(José): ', cantar_parabens('José'))
print('cantar_parabens(Augusto): ', cantar_parabens('Augusto'))

# Funções podem ter n parâmetros de entrada (eles são separados por vírgula):
print('\nFunções podem ter n parâmetros de entrada (eles são separados por vírgula):')

# Exemplo 03


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg


print("""
def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg
""")


print('soma(a=2, b=5): ', soma(a=2, b=5))

print('\nmultiplica(a=2, b=5): ', multiplica(a=2, b=5))

print('\noutra(a=2, b=5): ', outra(a=2, b=5, msg='Oi '))

# Exemplo 04 (A ordem importa se os parâmetros não forem declarados)
print('\nExemplo 04 (A ordem importa se os parâmetros não forem declarados)')


def nome_completo(nome, sobrenome):
    return f'\nO nome completo é: {nome} {sobrenome}.'


nome = 'Felicity'
sobrenome = 'Jones'


print("""
def nome_completo(nome, sobrenome):
    return f'O nome completo é: {nome} {sobrenome}.'
    
nome = 'Felicity'
sobrenome = 'Jones'
""")

print('nome_completo(nome, sobrenome): ', nome_completo(nome, sobrenome))
print('\nnome_completo(sobrenome, nome): ', nome_completo(sobrenome, nome))


# Exemplo 05 (A ordem NÃO importa quando se usa argumentos nomeados (Keyword Arguments)
print('\nExemplo 05 (A ordem NÃO importa quando se usa argumentos nomeados (Keyword Arguments)')

print('\nnome_completo(nome=nome, sobrenome=sobrenome): ', nome_completo(nome=nome, sobrenome=sobrenome))
print('\nnome_completo(sobrenome=sobrenome, nome=nome): ', nome_completo(sobrenome=sobrenome, nome=nome))

# Erro comum na utilização do return
print('\nErro comum na utilização do return')


def soma_impares1(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        return total


def soma_impares2(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


print("""
Lembrete: O return finaliza a função, por isso, a primeira função está errada e a segunda certa.
def soma_impares1(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        return total


def soma_impares2(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total
    
lista = [1, 2, 3, 4, 5, 6, 7, 8]
""")

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print('soma_impares1(lista): ', soma_impares1(lista))
print('\nsoma_impares2(lista): ', soma_impares2(lista))
