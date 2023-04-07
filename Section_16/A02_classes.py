"""
POO - Classes

Em POO, classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Classes podem conter:
- Atributos: representam as características do objeto. Pelos atributos conseguimos representar computacionalmente
os estados de um objeto. No caso da lâmpada, possivelmente, iríamos querer saber a voltagem, a luminosidade,
se é branca ou amarela, etc.

- Métodos (funções) -> representam os comportamento do objeto, ou seja, as ações que este objeto pode realizar
no sistema. No caso da lâmpada um comportamento seria ligar e desligar a lâmpada.


OBS1: utilizamos a palavra pass em Python quando temos um bloco de código que ainda não está implementado.

OBS2: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maicúlculo, todas juntas.

OBS3: Classes internas do Python são com letras minúsculas. Ex. int, str, float.

OBS4: Quando estamos planejando um software e definimos quais calasses teremos que ter no sistema,
chamamos estes objetos que serão mapeados para classes de entidade. Lampada é uma entidade no exemplo abaixo.
"""

# Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.


class Lampada:
    pass


lamp = Lampada()

print('type(lamp): ', type(lamp))


class ContaCorrente:
    pass




