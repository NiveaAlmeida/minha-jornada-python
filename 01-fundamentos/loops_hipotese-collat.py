c0 = int(input('Digite um número: '))
etapas = 0
while c0 !=1: #Enquanto for diferenete de 1
  if c0 % 2 ==0: #Se for par
    c0 = c0 // 2 #Divisão gerando um resultado inteiro
    print(c0)
    etapas += 1
  else: #Se for impar
    c0 = 3 * c0 + 1
    print(c0)
    etapas += 1
print(f'Etapas: {etapas}')
