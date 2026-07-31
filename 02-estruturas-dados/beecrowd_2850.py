condicoes = {
    'esquerda': 'ingles',
    'direita': 'frances',
    'nenhuma': 'portugues',
    'ambas': 'caiu'
}
condicao = input('Digite a condição: ').strip().lower()
print(condicoes[condicao])
