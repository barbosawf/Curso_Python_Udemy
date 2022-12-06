# import os
# os.system('cls' if os.name == 'nt' else 'clear')

nome = str(input("Qual é o seu nome? "))
print(f'Bem-vindo, {nome}!')
idade = int(input("Qual é a sua idade? "))
print("%s, você tem %s anos de idade." % (nome, idade))
print('{0}, você tem {1} anos de idade.' .format(nome, idade))

# cast é a conversão de um tipo de dado para outro.

num = input()
a = int(num)
print(type(num))
print(type(a))
