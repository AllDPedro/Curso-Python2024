def fibonacci(n):
  """Gera os n primeiros números da sequência de Fibonacci.

  Args:
    n: O número de termos da sequência a serem gerados.

  Returns:
    Uma lista contendo os n primeiros números da sequência de Fibonacci.
  """

  if n <= 0:
    return []  # Se n for menor ou igual a zero, retorna uma lista vazia

  # Inicializa a sequência com os dois primeiros termos
  fib = [0, 1]

  # Gera os demais termos da sequência
  while len(fib) < n:
    fib.append(fib[-1] + fib[-2])

  return fib

# Solicita o número de termos ao usuário
n = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Chama a função e imprime a sequência
resultado = fibonacci(n)
print("Sequência de Fibonacci:", resultado)