numero = int(input("Digite um número inteiro positivo: "))
contador = 1 #Começa com o numero 1
while contador <= numero: # Irá contar até o número
  if contador % 2 != 0: #Imprime somente os números ímpares
    print(contador) 
  contador += 1
