def soma_ate(numero):
  """Calcula a soma de todos os números inteiros de 1 até o número informado.

  Args:
    numero: O número final da soma.

  Returns:
    Uma string com a expressão completa da soma e o resultado.
  """

  soma = 0
  expressao = ""
  for i in range(1, numero + 1):
    expressao += str(i)
    if i < numero:
      expressao += " + "
    soma += i
  return f"{expressao} = {soma}"

# Solicita o número ao usuário
num = int(input("Digite um número: "))

# Chama a função e imprime o resultado
resultado = soma_ate(num)
print(resultado)