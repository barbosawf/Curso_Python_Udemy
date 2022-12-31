"""
Reversed

OBS. Não confundir com a função reverse() visto na lista, pois a função reverse() só funciona na lista.
Função é inverter o iterável.
"""

# Exemplo 01
print('Exemplo 01')

list_num = [1, 2, 3, 4, 5]
tupl_num = (1, 2, 3, 4, 5)

print("""list_num = [1, 2, 3, 4, 5]
tupl_num = (1, 2, 3, 4, 5)
""")

print('reversed(list_num): ', reversed(list_num))
print('list(reversed(list_num)): ', list(reversed(list_num)))

print('\nreversed(tupl_num): ', reversed(tupl_num))
print('list(reversed(tupl_num)): ', list(reversed(tupl_num)))

'''set_num = {1, 2, 3, 4, 5}
dic_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}'''

# Exemplo 02. Iterar sobre reversed
print('\nExemplo 02. Iterar sobre reversed')

print("""
for letra in reversed('Geek University'):
    print(letra, end=' ') 
print('')
""")

for letra in reversed('Geek University'):
    print(letra, end=' ')
print('')

# Exemplo 03. Iterar sobre reversed
print('\nExemplo 03. Iterar sobre reversed')
print("print(''.join(list(reversed('Geek University')))): ")
print(' '.join(list(reversed('Geek University'))))

# Exemplo 04.
print('\nExemplo 04')

print(list(reversed((range(0, 10)))))
