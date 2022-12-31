"""
all() Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
any() Renorna True se algum dos elementos do iterável é verdadeiro. Se o iteráve estiver vazio, retorna False.
"""

# Exemplo 01. all()
print('Exemplo 01. all()')

print('all([0, 1, 2, 3, 4]): ', all([0, 1, 2, 3, 4]), '\nO resultado é falso porque o zero é falso em Python.')

print('\nall([5, 1, 2, 3, 4]): ', all([5, 1, 2, 3, 4]), '\nO resultado é verdadeiro, pois todos os elementos o são.')

print('\nall([]): ', all([]), '\nO resultado é verdadeiro.')

print('\nall(()): ', all(()), '\nO resultado é verdadeiro.')

print('\nall("Geek"): ', all("Geek"), '\nO resultado é verdadeiro.')

# Exemplo 02. all()
print('\nExemplo 02. all()\n')

nomes1 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
nomes2 = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Lorena']

print("nomes1: ", nomes1)
print("[nome[0] == 'C' for nome in nomes1]: ", [nome[0] == 'C' for nome in nomes1])
print("all(nome[0] == 'C' for nome in nomes1): ", all(nome[0] == 'C' for nome in nomes1))

print("\nnomes2: ", nomes2)
print("[nome[0] == 'C' for nome in nomes2]: ", [nome[0] == 'C' for nome in nomes2])
print("all(nome[0] == 'C' for nome in nomes2): ", all(nome[0] == 'C' for nome in nomes2))

# Exemplo 03. all()
print('\nExemplo 03. all()\n')

res1 = [1 if letra in 'aeiou' else 0 for letra in 'oie']
res2 = [1 if letra in 'aeiou' else 0 for letra in 'jiw']

print("""
res1 = [1 if letra in 'aeiou' else 0 for letra in 'oie']
res2 = [1 if letra in 'aeiou' else 0 for letra in 'jiw']
""")

print('res1: ', res1)
print('res2: ', res2)

print('\nall(res1): ', all(res1))
print('all(res2): ', all(res2))

# Exemplo 04. all()
print('\nExemplo 04. all()')

print('all([num for num in [4, 2, 10, 6, 8] if not num % 2]): ',
      all([num for num in [4, 2, 10, 6, 8] if not num % 2]))


# Exemplo 05. any()
print('\nExemplo 05. all()')

print('any([1, 2, 3, 4, 5]): ', any([1, 2, 3, 4, 5]))
print('any([0, 2, 3, 4, 5]): ', any([0, 2, 3, 4, 5]))
print('any([]): ', any([]))
print('any([0, False, {}, (), []]): ', any([0, False, {}, (), []]))
print('any([0, False, {}, (), [], 1]): ', any([0, False, {}, (), [], 1]))

# Exemplo 06. any()
print('\nExemplo 06. all()')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Lorena']

print("\nnomes: ", nomes)
print("[nome[0] == 'C' for nome in nomes]: ", [nome[0] == 'C' for nome in nomes])
print("any([nome[0] == 'C' for nome in nomes]): ", any([nome[0] == 'C' for nome in nomes]))

# Exemplo 07. any()
print('\nExemplo 07. all()')

print('\nany([num for num in [4, 2, 10, 6, 8] if not num % 2]): ',
      all([num for num in [4, 2, 10, 6, 8] if not num % 2]))

print('\nany([num for num in [4, 2, 10, 6, 8, 7, 9] if not num % 2]): ',
      all([num for num in [4, 2, 10, 6, 8, 7, 9] if not num % 2]))
