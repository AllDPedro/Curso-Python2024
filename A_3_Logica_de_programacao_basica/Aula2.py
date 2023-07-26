## Quebradores de linhas no código \r \n -> CRLF
## \n -> LF
# Exemplo abaixo 

print("Oi pessoal, tenho 24 anos e me chamo Allan Delon Pedro,\n e como vocês se chamam?")
# Geralmente é usado para cortar a mensagem e mandar para a proxíma linha do código.

## print é para exibir na tela e depois dela vem os argumentos, abaixo estão argumentos não nomeados.
print(12, 34, sep="-", end='\n\r')
print(15, 54, sep='-', end='\n')
print(16, 51, sep='-', end='\r')
## \r não funciona no windows.
## argumento sep= serve para colocar algo no lugar do espaço das linhas acima, ele quebra a linha.

