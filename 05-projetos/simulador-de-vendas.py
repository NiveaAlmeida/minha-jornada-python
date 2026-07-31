import numpy as np
import matplotlib.pyplot as plt

#Dicionário com as empresas
dados_de_vendas = {
    'Empresa A': [],
    'Empresa B': [],
    'Empresa C': [],
    'Empresa D': []
}

total = 0.0
mes = np.random.choice([30, 31])
vendas_por_dia = {dia: {} for dia in range(1, mes+1)} # Cria o dicionário com as vendas por dia, no mês

# Gera as vendas por dia aleatoriamente
for dia in range(1, mes+1):  # começa em 1, não em 0
    for empresa in dados_de_vendas:
        vendas = float(np.random.randint(1, 20))
        dados_de_vendas[empresa].append(vendas) #Adiciona a venda no dicionário na chave de cada empresa
        vendas_por_dia[dia][empresa] = vendas #Cria uma chave por empresa a cada dia e adiciona a venda
        total += vendas
print()

# Gera e imprime os totais por empresa
print('Total de vendas por empresa no mês:')
for empresa, vendas_lista in dados_de_vendas.items():
    total_empresa = sum(vendas_lista)
    print(f'- {empresa}: {total_empresa:.2f}')
  
print(f'\nO total de vendas de todas as empresas foi: {total:.2f}')
print()

#Calculos estatísticos sobre as vendas
for empresa, vendas_lista in dados_de_vendas.items(): # para cada empresa
    vendas_np = np.array(vendas_lista) #cria um array com as vendas de cada empresa
    media_vendas = np.mean(vendas_np) # calcula a média de ventas
    dia_maior_venda_idx = np.argmax(vendas_np) #Índice do maior valor, ou seja, o dia
    dia_maior_venda = dia_maior_venda_idx + 1 #Adiciona mais 1, pois começa por 0 e não existe dia 0
    valor_maior_venda = vendas_np[dia_maior_venda_idx] #Valor da maior venda
    print(f'- {empresa}: Média diária = {media_vendas:.2f}, Dia com maior venda = {dia_maior_venda} ({valor_maior_venda:.2f})')

print()

dias = list(vendas_por_dia.keys()) #Cria uma lista com os dias
totais_por_dia = [sum(vendas_por_dia[dia].values()) for dia in dias] #Soma os valores por dia de todas as empresas


plt.plot(dias, totais_por_dia, marker='o') #Gráfico de linhas
plt.title("Vendas totais por dia")
plt.xlabel("Dias")
plt.ylabel("Vendas")
plt.grid(True)
plt.show()
