"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do código.

Erros mais comuns são:

1 — SyntaxError → Ocorre quando o Python encontra um erro de sintaxe. Algo que o Python não reconhece como parte da
linguagem.

a) Definir a função de forma errada.
def func:
    print('Geek University')

b) Atribuir valores a palavras reservadas.
None = 1

def = 1

c) return é esperado apenas dentro de uma função
return

2 - NameError → Ocorre quando uma variável ou função não é definida.

a)
print(geek)

b) Executar uma função que não foi definida.
geek()

c) Comum em variáveis locais
a = 18

if a < 10:
    msg = 'É menor que 10'

print(msg) # msg não existe porque a é maior que 10 e não menor.

3 - TypeError → Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a) O objeto do tipo 'int' não tem len(), pois precisa ser um iterável.
print(len(5))

b) Não é possível concatenar uma string e uma lista vazia.
print('Geek' + [])

4 - IndexError → Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
com índice errado.

a) O número dos índices são maiores daqueles possíveis.

lista = ['Geek']
print(lista[3])
print(lista[0][10])

5 - ValueError → Ocorre quan uma função/operação built-in (integrada) recebe um argumento com tipo correto,
mas valor inapropriado.

a) O argumento é correto, pois é uma string, mas neste caso não dá para converter 'Geek' em inteiro.
print(int('Geek'))
print(float('Geek'))

6 - ValueError → Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
a)

dic = {'Uni': 'Geek University'}
print(dic['Une'])

7 - AtributeError → Ocorre quando uma variável não tem um atributo/função.

a) Não existe a função sort() para a categoria de dado tupla.
tupla = (11, 2, 3, 6)
tupla.sort()

8 - IndentationError → Ocorre quando não respeitamos a indentação do Python que é 4 espaços.

a)
def nova():
print('Geek')

for i in range(10):
c = i + 1


OBS.: Exceptions e Erros são sinônimos na programação.
"""
