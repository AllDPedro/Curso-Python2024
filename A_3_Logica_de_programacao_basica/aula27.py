"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade
de caracteres da str
"""
variavel = 'Olá mundo'
## ao utilizar [-8:-2] ele vai mostrar desde o
## - 8 letra até o -2
print(variavel[-8:-2])
## ao adicionar len ele conta os caracteres
print(len(variavel))
## ele vai pegar apenas as letras dos [0:9:3]
print(variavel[0:9:3])
## tem como inverter também o texto [::-1]
print(variavel[::-1])