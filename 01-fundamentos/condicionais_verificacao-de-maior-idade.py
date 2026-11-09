# ---------------------------------------------------------
# Abordagem 1: Usando condicionais nativa do Python
# ---------------------------------------------------------

i1, i2, i3 = input("Digite três idades, separadas por vírgula: ").split(", ") #Recebe os valores das idades em string. A função split() irá separar a string em pedaços, nesse caso o ponto de corte será ", ", separando a string adquirida em três variáveis
#Transformar os dados de string para int
i1 = int(i1) 
i2 = int(i2)
i3 = int(i3)
#Estrutura condicional que irá comparar as idades e retornar a maior
if i1 > i2 and i1 > i3:
  print(f"A maior idade é {i1}")
elif i2 > i1 and i2 > i3:
    print(f"A maior idade é {i2}")
else:
    print(f"A maior idade é {i3}")

# ---------------------------------------------------------
# Abordagem 2: Usando uma variável maior_numero
# ---------------------------------------------------------

i1, i2, i3 = input("Digite três idades, separadas por vírgula: ").split(", ")
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)

maior_idade = i1 #Estabelece uma variável, indicando a primeira idade como a maior

#Condicionais que irão, se for o caso, alterar a variável maior_idade
if i2 > maior_idade:
    maior_idade = i2
if i3 > maior_idade:
    maior_idade = i3
print(f"A maior idade é {maior_idade}")

# ---------------------------------------------------------
# Abordagem 3: Usando a função max()
# ---------------------------------------------------------

i1, i2, i3 = input("Digite três idades, separadas por vírgula: ").split(", ") 
i1 = int(i1)
i2 = int(i2)
i3 = int(i3)
print(f"A maior idade é {max(i1, i2, i3)}") #Uso da funçaõ nativa max(), que retorna o maior elemento entre as variáveis indicadas.
