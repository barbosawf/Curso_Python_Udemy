"""
Geradores
- São iterators;
OBS: O contrário não é verdadeiro, ou seja, nem to-do iterator é um generator.

Outras informações:
-Generators podem ser criados com funções geradores;
- Funções geradorea utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras

Difereças entre Funções e Generator Functions (Funções Geradoras)

----------------------------------------------------------------------------------------
| Funções                                     | Generator Functions            |
----------------------------------------------------------------------------------------
| utilizam return                             | utilizam yield
----------------------------------------------------------------------------------------
| retorna uma vez                             | pode utilizar yield várias vezes |
---------------------------------------------------------------------------------------|
| quando executada, retorna um valor          | quando executada, retorna um generator |
---------------------------------------------------------------------------------------

"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo de Generator Function:
print(f'\n{a}Exemplo de Generator Function:{c}')


def conta_ate(valor_maximo):
    cont = 1
    while cont <= valor_maximo:
        yield cont
        cont += 1


print(f"""{b}
def conta_ate(valor_maximo):
    cont = 1
    while cont <= valor_maximo:
        yield c
        cont += 1{c}
""")

gen = conta_ate(5)

print(f"""
gen = conta_ate(5)

gen = {gen}

type(gen) = {type(gen)}
""")

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(f"""{b}
gen = conta_ate(10)

for num in gen:
    print(num)
{c}""")

gen = conta_ate(10)

for num in gen:
    print(num)


# Cuidado ao usar next() e depois o for:
print(f'\n{a}Cuidado ao usar next() e depois o for:{c}')


print(f"""{b}
gen = conta_ate(10)

print(next(gen))

print('Geek')

for i in gen:
    print(i){c}
""")

gen = conta_ate(10)

print(next(gen))

print('Geek')

for i in gen:
    print(i) # começa a partir do 2


# Gerar tudo de uma vez:
print(f'\n{a}Gerar tudo de uma vez:{c}')


print(f"""{b}
gen = list(conta_ate(10))  # para gerar todos os números de uma vez, usa-se a função list()

print(gen)
{c}""")

gen = list(conta_ate(10))

print(gen)
