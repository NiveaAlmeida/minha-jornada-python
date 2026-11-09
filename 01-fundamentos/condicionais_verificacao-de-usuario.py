admins =['ana@empresa.com','guilherme@empresa.com', 'felipe@empresa.com']
usuario = input('Insira o seu email: ').lower().strip()
if usuario in admins:
  print('Acesso liberado! Bem-vindo ao painel de controle')
else:
  print('Acesso negado. Você não tem permissões de administrador')
