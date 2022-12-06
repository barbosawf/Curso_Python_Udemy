"""
Estruturas lógicas: and, or, not, is.

Operadores unários:
    - not,
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True.
Para o 'or', um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido.
"""
from random import sample

ativo = bool(sample([0, 1], k=1)[0])

logado = bool(sample([0, 1], k=1)[0])

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')

if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else:
    print('Bem-vindo usuário!')

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else:
    print('Bem-vindo usuário!')

print('Ativo is False?')
print(ativo is False)

print('Logado is True?')
print(logado is True)

nome = 'Geek'

print(nome is 'Geek')
