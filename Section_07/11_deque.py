"""
Módulo Collections - Deque

O Deque é uma lista de alto desempenho.
"""

# Fazendo o import
print('Fazendo o import.')
from collections import deque
print('from collections import deque')

# Criando deques e listas:
print('\nCriando deques e listas')

deq = deque('geek')
print("deq = deque('geek')")
print('deq: ', deq)
print('')
lista = list('geek')
print("lista = list('geek')")
print('lista: ', lista)

# Adicionar elementos no deque e na lista
print('\nAdicionar elementos no deque e na lista:')
deq.append('y')
print("deq.append('y')")
print('deq: ', deq)
print('')
lista.append('y')
print("lista.append('y')")
print('lista: ', lista)
print('')
deq.appendleft('k')
print("deq.append('k')", 'A opção lefappend só tem no deque')
print('deq: ', deq)
print('')


# Remover elementos no deque e na lista
print('\nRemover elementos no deque e na lista:')
deq.pop()
print("deq.pop()")
print('deq: ', deq)
print('')
lista.pop()
print("lista.pop()")
print('lista: ', lista)
print('')
deq.popleft()
print("deq.popleft()", 'A opção lefpop só tem no deque')
print('deq: ', deq)

# A remoção pode ser dentro do comando print
print('\nA remoção pode ser dentro do comando print')

print('lista.pop(): ', lista.pop())
print('deq.pop(): ', deq.pop())

print('\nlista: ', lista)
print('deq: ', deq)

