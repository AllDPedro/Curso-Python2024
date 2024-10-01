# Operadores in e not in
# Strings são interáveis
#  0 1 2 3 4
#  D e l o n
# -5-4-3-2-1

# nome = 'Delon'
# print(nome[2]) # Checando letra por letra com o []
# # Checar letra por letra no nome
# print('n' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Deseje o que quer encontrar no seu nome:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')