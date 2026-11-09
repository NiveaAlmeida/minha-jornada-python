num = float(input("Digite um número: "))
if num > 0:
  if num % 2 == 0 and num % 5 == 0: #Se é divisível por dois e por cinco
    print(f"O número é positivo, par e múltiplo de cinco")
  elif num % 2 == 0: #Se é divisível somente por 2
    print("O número é positivo e par")
  else:
    print("O número é positivo e impar")
elif num == 0:
  print("O número é zero")
else:
  print("O número é negativo")
