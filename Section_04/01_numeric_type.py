"""
Tipo numérico

print("\x1b[2J\x1b[1;1H", end="")
"""

print(1_000_000)

num = 42
print(num)
num -= 5
print(num)
num *= 2
print(num)
num /= 3
print(num)
num %= 2
print(num)

type(num)

dir(num)

"""
Digitar no terminal: dir(num) irá mostrar todas as operações possíveis com num.
"""

print(num.__add__(8))
