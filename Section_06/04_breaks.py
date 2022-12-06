"""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 01
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)

# Exemplo 02

while True:
    comando = str(input('Digite "sair" para sair: ')).strip().lower()
    if comando == 'sair':
        break

