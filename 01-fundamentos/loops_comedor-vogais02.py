word_without_vowels = ""
user_word = input('Insira uma palavra: ').upper()

for letter in user_word:
    if letter in 'AEIOU':
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
