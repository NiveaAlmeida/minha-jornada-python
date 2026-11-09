def contador_de_letras(palavra, letra):
  """Conta quantas vezes uma letra aparece em uma palavra.
  args:
    palavra (str): A palavra na qual a letra será contada.
    letra (str): A letra que será contada na palavra.
    returns:
    int: O número de vezes que a letra aparece na palavra.
    """
  contador = 0
  palavra = palavra.lower()
  for letras in palavra:
    if letras == letra:
      contador += 1
  return contador

def conversor_para_maisculas(frase):
    """Converte uma frase para maiúsculas.
    Args:
        frase (str): A frase a ser convertida.
    Returns:
        str: A frase convertida para maiúsculas.
    """
    return frase.upper()

palavra = input('Digite uma palavra: ')
letra = input("Qual letra deseja contar?: ")
quantidade_de_letras = contador_de_letras(palavra, letra)
print(f"A letra '{letra}' aparece {quantidade_de_letras} vezes na palavra '{palavra}'.")

frase = input("Digite uma frase para converter em maiúsculas: ")
frase_maiuscula = conversor_para_maisculas(frase)
print("Frase em maiúsculas:", frase_maiuscula)
