"""
Programação orientada a objetos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para modelos computacionais.

Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemaas.
Python suporta vários tipos de paradígmas de programação:

Principais elementos da POO
- Classe: modelo do objeto do mundo real sendo representado computacionamemente.
- Atributo: característica do objeto.
- Método: comportamento do objeto (funções)
- Construtor: método especial utilizado para criar os objetos
- Objeto: instância da classe.

Se escrevemos as nossas classes, estamos criando o tipo do objeto.
Exemplos:

numero = 10  # cria um objeto do tipo inteiro
nome = 'Geek'  # cria um objeto do tipo string.

class Produto:
    pass

ps4 = Produto()

criou-se um produto chamado ps4 e utilizou-se o construtor da classe Produto para criar ps4.


1) Programação orientada a objetos: objetivo é mapear objetos do mundo real para modelos computacionais,
fazendo com que possamos representar tais objetos com suas características e comportamentos.

Exemplo:

Classe produto pode ter 3 atributos (nome, preço, desconto).
Métodos são o comportamento do objeto (lembrar de função). O método está dentro de uma classe.
Uma função dentro da classe é um método.

Construtor também é um método, mas é um método especial. Serve para criar um objeto a partir da classe.
2) Programação estruturada
3) Programação funcional
"""

numero = 10  # cria um objeto do tipo inteiro
print('numero: ', numero)
print('type(numero): ', type(numero))

nome = 'Geek'  # cria um objeto do tipo string.
print('\nnome: ', nome)
print('type(nome): ', type(nome))


class Produto:
    pass


ps4 = Produto()
print('\nps4: ', ps4)
print('type(ps4): ', type(ps4))
