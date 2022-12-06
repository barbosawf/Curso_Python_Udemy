"""
Loop for
loop -> ? uma estrutura de repeti??o
for -> ? uma dessas estruturas

C ou Java
for (int i == 0; i < limitador; i++) {
    //execu??o
}

Python

for ?tem in inter?vel:
    //execu??o do loop

Utilizamos loops para iterar sobre sequ?ncias ou sobre valores iter?veis.

Exemplos de iter?veis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    range(1, 10)

Tabela de Emojis Unicode: https://apps.timwhilock.info/emoji/tables/unicode
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(i, '', v)

for _, v in enumerate(nome):  # o underline descarta (neste caso o ?ndice)
    print(v)

for i, _ in enumerate(nome):  # o underline descarta (neste caso o string)
    print(i)

for a in enumerate(nome):
    print(a)

for a in enumerate(nome):  # retorna os ?ndices
    print(a[0])

for a in enumerate(nome):  # retorna as letras
    print(a[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd + 1):
    print(n)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma ? {soma}')

print(nome * 3)

# Original: U+1F60D
# Modificado: U0001F60D

emoji = '\U0001F60D'

print(emoji)

for i in range(1, 11):
    print(f'{emoji * i}')

emoji = '\U0001F60D'
for _ in range(3):
    for i in range(1, 11):
        print(f'{" " * (10 - i)}{emoji * i}')

print()

for j in range(3):
    a = 10 + j * 2
    for i in range(1, a):
        if j == 0:
            b = 1
        else:
            b = 0
        print(f"{' ' * (13 - i - b)}{emoji * i}")
