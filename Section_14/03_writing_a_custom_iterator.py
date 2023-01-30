"""
Escrevendo um iterador customizado
# quando há uma função dentro de uma classe, o primeiro parâmetro é o self, que representa o próprio objeto.
na função, os atributos da classe são maior e menor
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


con = Contador(1, 5)

print(con, '\n')

for n in Contador(1, 10):
    print(n)




