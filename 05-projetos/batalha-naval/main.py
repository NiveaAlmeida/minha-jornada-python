from tabuleiro import *
from embarcacao import *

frota_posicionada = []


def jogar_batalha_naval(linhas, colunas, frota_posicionada):
    """Inicia o jogo de batalha naval.

    Args:
        linhas (int): O número de linhas do tabuleiro.
        colunas (int): O número de colunas do tabuleiro.
        frota_posicionada (list): Lista de navios posicionados
    """
    tabuleiro = criar_tabuleiro(linhas, colunas)

    while True:
        mostrar_tabuleiro(tabuleiro)
        print("\nDigite uma posição para revelar (ou 'sair' para encerrar):")
        entrada = input("Linha e Coluna (ex: '1 a'): ").strip().lower()

        if entrada == 'sair':
            print("Saindo do jogo...")
            break

        try:
            linha_str, coluna_letra = entrada.split()
            linha = int(linha_str)
            coluna = letra_para_coluna(coluna_letra, colunas)

            if not verificar_posicao(tabuleiro, linha, coluna):
                print("Coordenadas inválidas! Tente novamente.")
                continue

            if verificar_revelacao(tabuleiro, linha, coluna):
                print("Posição já revelada! Tente novamente.")
                continue

            acertou = False
            for navio in frota_posicionada:
                if navio.registrar_ataque(linha, coluna):
                    acertou = True
                    tabuleiro[linha][coluna] = 'X'  # 'X' para marcar acerto
                    if navio.verificar_afundada():
                        print(f'O navio {navio.nome} foi afundado(a)!')
                    else:
                        print(f'O navio {navio.nome} foi atingido(a)!')
                    break
            if not acertou:
                print("Errou!")
                tabuleiro[linha][coluna] = 'O'  # 'O' para marcar água/erro

            if verificar_vitoria(frota_posicionada):
                mostrar_tabuleiro(tabuleiro)
                print("Parabéns! Você venceu o jogo!")
                break
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar no formato correto.")

inicio = input("Deseja iniciar o jogo de Batalha Naval? (s/n): ").strip().lower()

if inicio == 's':
    linhas = int(input("Digite o número de linhas do tabuleiro: "))
    colunas = int(input("Digite o número de colunas do tabuleiro: "))
    frota_filtrada = filtrar_frota(frota, linhas, colunas)
    for nome, tamanho in frota_filtrada.items():
        navio = posicionar_aleatoriamente(nome, tamanho, linhas, colunas, frota_posicionada)
        frota_posicionada.append(navio)
    jogar_batalha_naval(linhas, colunas, frota_posicionada)
else:
    print("Jogo encerrado.")