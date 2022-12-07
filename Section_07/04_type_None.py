"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio.
Falar tipo sem tipo é mais apropriado.
O tipo None é sempre especificado com a primera letra maiúscula.

Quando utilzamos?

- Podemos utilzar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de receber
um valor final.

OBS.: O tipo None em Python é sempre considerado como False
"""

numeros = None
print(numeros)
print(type(numeros))

numeros = 1.44, 1.34, 5.67

print(numeros)
print(type(numeros))

# OBS.: O tipo None em Python é sempre considerado como False
print('\nOBS.: O tipo None em Python é sempre considerado como False')
print("""
Exemplo 01
a = None
if a:
    print('Sim')
else:
    print("Não")
""")

a = None
if a:
    print('Sim')
else:
    print("Não")

print('\nExemplo 02')
print("""
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

pais = paises.get('ru')
if pais:
    print('Encontrei o país!')
else:
    print("Não encontrei o país!")
""")
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

pais = paises.get('ru')
if pais:
    print('Encontrei o país!')
else:
    print("Não encontrei o país!")