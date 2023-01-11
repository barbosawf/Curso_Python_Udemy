def quadrado(n):
    return n * n


def soma_impares2(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


def soma_todos_numeros(*args):
    return sum(args)
