from tabuleiro import *
from embarcacao import *
from salvamento import *

frota_posicionada = []


def menu():
    """Exibe o menu de opções para o jogador."""
    print(f"""
{'-' * 38}
Bem vindo(a) ao jogo de Batalha Naval!
{'-' * 38}
O que deseja fazer?
1 - Novo jogo
2 - Jogar / Continuar
3 - Salvar jogo
4 - Carregar jogo
5 - Sair
{'-' * 38}
""")


def loop_jogo(tabuleiro, frota_posicionada):
    """Executa o loop de ataques da partida atual."""
    while True:
        mostrar_tabuleiro(tabuleiro)
        print("\nDigite uma posição para revelar (ou 'sair' para voltar ao menu):")
        entrada = input("Linha e Coluna (ex: '1 a'): ").strip().lower()

        if entrada == 'sair':
            print("Voltando ao menu...")
            break

        try:
            linha_str, coluna_letra = entrada.split()
            linha = int(linha_str)
            coluna = string.ascii_lowercase.index(coluna_letra)

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
                    tabuleiro[linha][coluna] = 'X'
                    if navio.verificar_afundada():
                        print(f'O navio {navio.nome} foi afundado(a)!')
                    else:
                        print(f'O navio {navio.nome} foi atingido(a)!')
                    break

            if not acertou:
                print("Errou!")
                tabuleiro[linha][coluna] = 'O'

            if verificar_vitoria(frota_posicionada):
                mostrar_tabuleiro(tabuleiro)
                print("Parabéns! Você venceu o jogo!")
                break
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar no formato correto.")


def jogar_batalha_naval():
    """Controla o menu principal do jogo."""
    tabuleiro = None
    frota_posicionada = None

    while True:
        menu()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            linhas = int(input("Digite o número de linhas do tabuleiro: "))
            colunas = int(input("Digite o número de colunas do tabuleiro: "))
            tabuleiro = criar_tabuleiro(linhas, colunas)
            frota_posicionada = []
            for nome, tamanho in filtrar_frota(frota, linhas, colunas).items():
                navio = posicionar_aleatoriamente(nome, tamanho, linhas, colunas, frota_posicionada)
                frota_posicionada.append(navio)
            loop_jogo(tabuleiro, frota_posicionada)

        elif opcao == "2":
            if tabuleiro is None:
                print("Nenhum jogo em andamento.")
            else:
                loop_jogo(tabuleiro, frota_posicionada)

        elif opcao == "3":
            if tabuleiro is None:
                print("Nenhum jogo em andamento para salvar.")
            else:
                arq_tab = input("Nome do arquivo do tabuleiro (ex: tab.txt): ").strip()
                arq_gab = input("Nome do arquivo do gabarito (ex: gab.txt): ").strip()
                salvar_tabuleiro(tabuleiro, arq_tab)
                salvar_gabarito(frota_posicionada, arq_gab)
                print("Jogo salvo!")

        elif opcao == "4":
            arq_tab = input("Nome do arquivo do tabuleiro (ex: tab.txt): ").strip()
            arq_gab = input("Nome do arquivo do gabarito (ex: gab.txt): ").strip()
            try:
                tabuleiro = restaurar_tabuleiro(arq_tab)
                gabarito = carregar_gabarito(arq_gab)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            else:
                frota_posicionada = []
                for nome, posicoes in gabarito.items():
                    navio = Embarcacao(nome, len(posicoes))
                    navio.posicao = posicoes
                    navio.acertos = [(l, c) for (l, c) in posicoes if tabuleiro[l][c] == 'X']
                    if len(navio.acertos) == navio.tamanho:
                        navio.status = "afundada"
                    elif navio.acertos:
                        navio.status = "atingida"
                    frota_posicionada.append(navio)
                loop_jogo(tabuleiro, frota_posicionada)

        elif opcao == "5":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    jogar_batalha_naval()