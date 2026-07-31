quantidade = int(input("Digite a quantidade de números da sequência de Fibonacci que você quer ver: "))
a, b = 0, 1 #Começa com os dois primeiros números da sequência: 0 e 1
cont = 0
while cont < quantidade: # Enquanto o contador for menor que a quantidade
  print(a, end =", ") 
  a, b = b, a + b #Altera a para o antigo valor da variável b e, posteriormente, o valor de b para a soma entre a e b, aplicando a regra da sequência de Fibonacci
  cont += 1
