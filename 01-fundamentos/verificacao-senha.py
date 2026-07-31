#Cadastra uma senha e verifica se a pessoa colocou a senha correta, limite de 3 tentativas
cadastro_senha = input("Digite uma senha: ")
tentativa = 0
while input("Digite novamente a senha: ") != cadastro_senha:
  tentativa += 1
  if tentativa < 3: # Impõe o limite de tentativas
    print("As senhas não coincidem, digite a senha novamente")
  else:
    print("Você errou a senha três vezes, tente novamente mais tarde")
    break #Para o código se o limite for excedido
else:
  print("As senhas coincidem")
