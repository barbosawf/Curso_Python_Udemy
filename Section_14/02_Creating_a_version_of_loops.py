"""
Criando a própria versão de Python
"""


def meu_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(next(iterable))
        except StopIteration:
            break


meu_for('Wagner\n')


def meu_for_2(iterable):
    l = len(iterable)
    iterable = iter(iterable)
    c = 0
    while c < l:
        try:
            print(next(iterable))
        except StopIteration:
            break
        c += 1


meu_for_2('Faria')
print()
meu_for([1, 3, 4, 5])
print()
meu_for_2([9, 5, 4, 3])