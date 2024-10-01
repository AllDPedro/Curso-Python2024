clientes = []

def cadastrar_cliente():
  nome = input("Digite o nome do cliente: ")
  email = input("Digite o e-mail do cliente: ")
  telefone = input("Digite o telefone do cliente: ")

  cliente = {
    'nome': nome,
    'email': email,
    'telefone': telefone
  }

  clientes.append(cliente)
  print("Cliente cadastrado com sucesso!")

def listar_clientes():
  if not clientes:
    print("Não há clientes cadastrados.")
  else:
    print("\nLista de Clientes:")
    for cliente in clientes:
      print(f"Nome: {cliente['nome']}")
      print(f"E-mail: {cliente['email']}")
      print(f"Telefone: {cliente['telefone']}")
      print("-" * 20)

while True:
  print("\nMenu:")
  print("1. Cadastrar Cliente")
  print("2. Listar Clientes")
  print("3. Sair")

  opcao = input("Digite a opção desejada: ")

  if opcao == '1':
    cadastrar_cliente()
  elif opcao == '2':
    listar_clientes()
  elif opcao == '3':
    break
  else:
    print("Opção inválida!")