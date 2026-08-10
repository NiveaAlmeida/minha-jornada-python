palavra = input('Digite uma palavra: ').upper()
for letra in palavra:
    if letra in 'AEIOU':
      continue
    else:
      print(letra)
