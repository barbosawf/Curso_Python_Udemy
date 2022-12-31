"""
len, abs, sum, round
"""

# Exemplo 01.(len)
print('Exemplo 01.(len)')

print("len('Geek University'): ", len('Geek University'))
print('len([1, 2, 3, 4, 5]):   ', len([1, 2, 3, 4, 5]))
print('len((1, 2, 3, 4, 5)):   ', len((1, 2, 3, 4, 5)))
print('len(range(0, 10)):      ', len(range(0, 10)))

# Exemplo 02.(toda função Python que começa e termina com dois underlines é chamada de dunder. Neste caso dunder len)
print('\n# Exemplo 02.(toda função Python que começa e termina com dois underlines é chamada de dunder). '
      'Neste caso dunder len')
print("'Geek University'.__len__(): ", 'Geek University'.__len__())

# Exemplo 03.(abs)
print("\nExemplo 03.(abs)")

print('abs(-5):     ', abs(-5))
print('abs(5):      ', abs(5))
print('abs(-3.21):  ', abs(-3.21))

# Exemplo 04.(em sum o valor inicial é zero)
print("\nExemplo 04.(em sum o valor inicial é zero)")

print('sum([]):                    ', sum([]))
print('sum([1, 2, 3, 4, 5]):       ', sum([1, 2, 3, 4, 5]))
print('sum((1, 2, 3, 4, 5)):       ', sum((1, 2, 3, 4, 5)))
print('sum({1, 2, 3, 4, 5}):       ', sum({1, 2, 3, 4, 5}))
print('sum([1, 2, 3, 4, 5], 5):    ', sum([1, 2, 3, 4, 5], 5))
print('sum([1, 2, 3, 4, 5], -5):   ', sum([1, 2, 3, 4, 5], -5))

print("sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()):       ",
      sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Exemplo 04.(round)
print("\nExemplo 04.(round)")

print('round(-3.21367):  ', round(-3.21367))
print('round(9.871487):   ', round(9.871487))
print('round(10.0):       ', round(10.0))

print('\nround(-3.21367, 2):  ', round(-3.21367, 2))
print('round(9.271487, 2):   ', round(9.271487, 2))
print('round(10.0, 2):       ', round(10.0, 2))


