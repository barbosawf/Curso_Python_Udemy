"""
O block with é utilizado para criar um contexto de trabalho em que os recursos
utilizados são fechados após o bloco with.

Quando sai do with não existe mais o contexto, é como se fosse uma variável local.
"""
a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# O bloco with
print(f'{a}O bloco with{c}')

print(f"""{b}
with open('Texto_01.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed){c}
""")

with open('Texto_01.txt') as arquivo:
    print(arquivo.readlines())
    print('arquivo.closed: ', arquivo.closed)


print('\narquivo.closed: ', arquivo.closed)
