import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0
palpite = None

print('''
+--------------------------+
|    Seja Bem vindo ao     |
|   Jogo de Adivinhação!   |
+--------------------------+
''')
print("Tente adivinhar o número entre 1 e 100.")

palpite = int(input("Digite seu palpite: "))
while palpite != numero_aleatorio:
    palpite = int(input("Tente novamente:) "))
  
    if palpite < 1 or palpite > 100: # Verifica se o palpite está fora do intervalo
        print("Palpite inválido! Digite um número entre 1 e 100.")
        continue  # volta para o início do loop sem contar tentativa
    tentativas += 1
  
    if palpite < numero_aleatorio: #Imprime uma dica para o jogador
        print("O número correto é MAIOR.")
    elif palpite > numero_aleatorio:
        print("O número correto é MENOR.")

print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
