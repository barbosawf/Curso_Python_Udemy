"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', 's34', 'a', '42.3'
- Estiver entre aspas duplas -> "uma string", "s34", "a", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''s34''', '''a''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """s34""", """a""", """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Geek University"
print(nome)
print(type(nome))

nome = '''Geek University'''
print(nome)
print(type(nome))

nome = """Geek University"""
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = "Angelina \nJolie"
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

nome = "Geek University"
print(nome.upper())
print(nome.lower())
print(nome.split()) # transforma em uma lista de strings

print(nome[0])

print(len(nome))

print(nome[0:4])

print(nome.split()[0])

print(nome.split()[1])

print(nome[::-1])

print(nome.replace("G", "P"))

print(nome.replace("e", "i"))

print("Teste")
