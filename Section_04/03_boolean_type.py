"""
Tipo booleano
Álgebra booleana, criada por George Boole
2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso
"""

ativo1 = False
ativo2 = True

print(ativo1)
print(ativo2)

"""
Operações básicas
"""

# Negação (not):
"""
Fazendo a negação: se o valor booleano for verdadeiro o resultado será falso;
Se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print("Negação")
print(not ativo1)
print(not ativo2)

# Ou (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
"""
print("Ou")
print(True or True)
print(True or False)
print(False or False)


# E (and):

"""
É uma operação binária, ou seja, depende de doi valores.
Ambos os valores devem ser verdadeiros.
"""

print("E")
print(True and True)
print(True and False)
print(False and False)

# Operações booleanas:
print("5 > 6")
print(5 > 6)

print("5 < 6")
print(5 < 6)

print("5 == 6")
print(5 == 6)

print("5 == 5")
print(5 == 5)

print("5 <= 6")
print(5 <= 6)

print("5 >= 6")
print(5 >= 6)

num1 = 7
num2 = 8
print("num1 >= num2")
print(num1 >= num2)

print("num1 == num2")
print(num1 == num2)

print("num1 <= num2")
print(num1 <= num2)

print("num1 < num2 or num1 > 3")
print(num1 < num2 or num1 > 3)

print("num1 < num2 and num1 > 3")
print(num1 < num2 and num1 > 3)

print("type(ativo1)")
print(type(ativo1))

print("dir(ativo1)")
print(dir(ativo1))
