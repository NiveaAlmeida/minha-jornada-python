soma = 0
while True:
  numero = int(input("Digite um número inteiro positivo (ou um negativo para sair): "))
  if numero < 0: #Para o código se um número negativo for inserido
    break
  soma += numero
  print(f"Soma parcial atual: {soma}")
print(f"A soma dos números positivos é: {soma}")
