"""
Loop while

Forma geral
while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão cujo resultado é verdadeiro ou falso.
"""

num = 0

while num < 10:
    print(num)
    num += 1


resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ').strip().lower()