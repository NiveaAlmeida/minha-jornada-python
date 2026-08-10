turmas = []

numero_de_turmas = int(input("Digite o número de turmas: "))

for i in range(numero_de_turmas):
    turma = { "turma": i + 1, "alunos": {} } 
    turmas.append(turma)  
    numero_alunos = int(input(f'Insira o número de alunos na turma {i + 1}: '))
    
    for j in range(numero_alunos): 
        nome_aluno = input(f'Digite o nome do aluno {j + 1}: ')
        
        nota_1 = float(input(f'\nDigite a nota 1 de {nome_aluno}: '))
        nota_2 = float(input(f'\nDigite a nota 2 de {nome_aluno}: '))
        nota_3 = float(input(f'\nDigite a nota 3 de {nome_aluno}: '))
        
        turma['alunos'][nome_aluno] = {
            "nota_1": nota_1,
            "nota_2": nota_2,
            "nota_3": nota_3,
        }

for i in range(len(turmas)): 
    turma = turmas[i]
    print(f'\nTurma {i + 1}:')
    print(turma)

print()

# Cálculo da média e definição da situação para todos os alunos de todas as turmas
for turma in turmas:
    for aluno, notas in turma['alunos'].items():
        media_aluno = (notas["nota_1"] + notas["nota_2"] + notas["nota_3"]) / 3
        notas["media"] = media_aluno
        if media_aluno >= 7:
            notas["situacao"] = "Aprovado"
        elif media_aluno >= 5:
            notas["situacao"] = "Recuperação"
        else:
            notas["situacao"] = "Reprovado"

print()
print("Média e Situação dos Alunos:")
for turma in turmas:
    print(f"\nTurma {turma['turma']}:")
    for aluno, notas in turma['alunos'].items():
        print(f"{aluno}: Média = {notas['media']:.2f}, Situação = {notas['situacao']}")


# Cálculo das médias por turma
medias_turmas = []
for turma in turmas:
    total_alunos = len(turma['alunos'])
    soma_medias = sum(n["media"] for n in turma['alunos'].values()) if total_alunos > 0 else 0
    media_turma = soma_medias / total_alunos if total_alunos > 0 else 0
    turma["media_da_turma"] = media_turma
    medias_turmas.append(media_turma)

print()
print("\nMédias das Turmas:")
for i, media in enumerate(medias_turmas):
    print(f"Turma {i + 1}: {media:.2f}")
print()


# Pesquisa por aluno
turma_pesquisa = int(input("Digite a turma do aluno: ")) - 1
nome_pesquisa = input("Digite o nome do aluno que deseja pesquisar: ")


if nome_pesquisa not in turmas[turma_pesquisa]["alunos"]:
        print("Aluno não encontrado")
        nome_pesquisa = int(input("Digite novamente o nome do aluno: ")) - 1

if turma_pesquisa < 0 or turma_pesquisa >= len(turmas):
    print("Turma inválida. Por favor, insira 1, 2 ou 3.")
else:
    if nome_pesquisa not in turmas[turma_pesquisa]["alunos"]:
        print("Aluno não encontrado nessa turma.")
        turma_pesquisa = int(input("Digite o número da turma do aluno (1, 2 ou 3): ")) - 1
    else:
        print('Aluno encontrado!')
        dados = turmas[turma_pesquisa]["alunos"][nome_pesquisa]
print(f'O aluno {nome_pesquisa} da turma {turma_pesquisa + 1} tem as seguintes informações:')
print(f'Nota 1: {dados["nota_1"]}, Nota 2: {dados["nota_2"]}, Nota 3: {dados["nota_3"]}, Média: {dados["media"]:.2f}, Situação: {dados["situacao"]}')
