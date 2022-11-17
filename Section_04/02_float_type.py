"""
Tipo float
Tipo real ou decimal
obs.: o separador de casas decimais na programação é o ponto e não a vírgula
print("\x1b[2J\x1b[1;1H", end="")
"""
# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(type(valor))

# Certo do ponto de vista do Float
valor = 1.44
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44

print(valor1)

print(valor2)

# Podemos converter um float para um int
valor = 1.44
res = int(valor)
print(res)
print(type(res))

# Podemos converter um in para um float
valor = 20
res = float(valor)
print(res)
print(type(res))

# Podemos trabalhar com númeroc complexos (não é i, e sim j)
var = 5j
print(type(var))
