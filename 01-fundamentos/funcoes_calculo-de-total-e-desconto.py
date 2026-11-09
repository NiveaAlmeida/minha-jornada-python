def calculo_total_e_desconto(precos):
    """Calcula o valor total bruto e o valor total com desconto de uma lista de preços.

    Aplica faixas de desconto progressivas com base no valor individual do item:
    - Preços acima de R$ 40,00 recebem 5% de desconto.
    - Preços acima de R$ 20,00 até R$ 40,00 recebem 2% de desconto.
    - Preços iguais ou inferiores a R$ 20,00 não recebem desconto.

    Args:
        precos (list[float]): Lista contendo os preços dos produtos.

    Returns:
        tuple[float, float]: Uma tupla contendo:
            - total (float): A soma total dos preços originais.
            - total_com_desconto (float): A soma total final após aplicar os descontos.

    Raises:
        ValueError: Se houver algum preço negativo na lista informada.
    """
    total = 0.0
    total_com_desconto = 0.0
    desconto1 = 0.02  # 2%
    desconto2 = 0.05  # 5%

    for preco in precos:
        if preco < 0:
            raise ValueError(f"Preço inválido: {preco}")

        total += preco

        if preco > 40:
            valor_item_com_desconto = preco * (1 - desconto2)
        elif preco > 20:
            valor_item_com_desconto = preco * (1 - desconto1)
        else:
            valor_item_com_desconto = preco

        total_com_desconto += valor_item_com_desconto

    return total, total_com_desconto

entrada = input("Insira os preços separados por vírgula: ")

precos = []
for item in entrada.split(","):
    item_limpo = item.strip()
    if item_limpo:  # Garante que não é um espaço vazio
        precos.append(float(item_limpo))

print(precos)

total, total_com_desconto = calculo_total_e_desconto(precos)
print(f"Total Bruto: R$ {total_bruto:.2f} | Total com Desconto: R$ {total_final:.2f}")
