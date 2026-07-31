idas_a_feira = int(input("Quantidade de idas à feira: "))

for ida in range(idas_a_feira): # Itera para cada ida à feira
  quantidade_produtos = int(input("Quantidade de produtos: "))
  produto_preco = {}
  for produto in range(quantidade_produtos):
    produto, preco_s = input("Digite o produto e seu preço, exemplo: 'produto: preço': ").lower().split(": ")
    produto_preco[produto] = float(preco_s)

  quantidade_comprados = int(input("Quantos produtos a serem comprados? "))
  total = 0.0 # Initialize total for the current test case
  
  for produtos in range (quantidade_comprados):
    produto_a_comprar, qtd_s = input("Digite o produto a ser comprado e a quantidade, exemplo 'Produto: quantidade': ").lower().split(": ")
    quantidade = int(qtd_s)

    if produto_a_comprar in produto_preco:
      total += produto_preco[produto_a_comprar] * quantidade
    else:
      produto_a_comprar, qtd_s = input("Este produto não está na lista, tente novamente: ").lower().split(": ")
      quantidade = int(qtd_s)
  print(f"R$ {total:.2f}")
