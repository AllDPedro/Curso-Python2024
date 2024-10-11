nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    # Invertendo o nome
    nome_invertido = nome[::-1]

    # Contando espaços
    num_espacos = nome.count(" ")

    # Contando letras
    num_letras = len(nome) - num_espacos

    # Primeira e última letras
    primeira_letra = nome[0]
    ultima_letra = nome[-1]

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")

    if num_espacos > 0 :
        print(f'Seu nome contém {num_espacos} espaços')
    else:
        print(f'não contém espaços')
        print(f"Seu nome tem {num_letras} letras")
        print(f"A primeira letra do seu nome é {primeira_letra}")
        print(f"A última letra do seu nome é {ultima_letra}")
else:
    print("Desculpe, você deixou campos vazios.")