palavra_secreta = 'chupacabra'
tentativa = input('''
+-----------------------+
| Você está preso em um |
|         loop          |
+-----------------------+  

Para sair, tente adivinhar a palavra secreta.
Tentativa: 
''').lower()

while True:
    if tentativa != palavra_secreta:
        tentativa = input('Erro! Tente novamente: ').lower()
    else:
        break
print('Você saiu do loop com sucesso!')
