alunos_notas = {
    'Alice': [9, 7.5, 8.5],
    'Bruno': [7, 6.5, 8],
    'Clara': [8, 9, 9.5],
    'David': [5.5, 6, 7]
}
novas_notas = {
    'Alice': 7.5,
    'Bruno': 8,
    'Clara': 9,
    'David': 8
}

novos_alunos = {
    "Elena": [8.5, 9, 9.5, 7.5],
    "Felipe": [6.5, 6, 7, 8],
    "Gisele": [10, 9.5, 9, 9.5],
    "Hugo": [5, 5.5, 6, 6.5],
    "Iris": [7.5, 8, 8.5, 9]
}

alunos_notas.update(novos_alunos) #Atualiza o alunos_notas com o dicionário novos_alunos, porém se a chave (nome do aluno) já existe em alunos_notas, o valor dela será substituído pelo valor de novos_alunos

for aluno in novas_notas.keys(): #Para cada aluno que estiver no dicionário "novas_notas"
  if aluno in alunos_notas: #Se o aluno estiver no dicionário "alunos_notas"
    alunos_notas.update({aluno:alunos_notas[aluno]+[novas_notas[aluno]]}) #Atualiza o dicionário com a união dos vetores dos valores de cada chave de alunos_notas, com os valores de cada chave de novas_notas
  else: # Se o aluno não existe, cria uma nova entrada com a nota
    alunos_notas.update({aluno:[novas_notas[aluno]]})
print(alunos_notas)


aluno = input('Digite o nome do aluno a ser pesquisado: ')

if aluno in alunos_notas: #verifica se o aluno pesquisado existe
    notas = alunos_notas[aluno] #Pega as notas da chave do nome do aluno pesquisado
    media = sum(notas) / len(notas) #Pega a soma das notas e divide pelo total
    print(f'As notas de {aluno} são: {alunos_notas[aluno]}')
    print(f'A média de {aluno} é {media:.2f}') 
    
else:
  print('O aluno não está na lista')

#Para remover a menor nota
for aluno, notas_do_aluno in alunos_notas.items(): #aluno = chave, notas_do_aluno = valor
    menor_nota = min(notas_do_aluno)
    notas_do_aluno.remove(menor_nota)
print(f'Notas dos alunos pós remoção: {alunos_notas}')
