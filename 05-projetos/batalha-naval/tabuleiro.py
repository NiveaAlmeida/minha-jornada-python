__all__ = [
    "criar_tabuleiro",
    "mostrar_tabuleiro",
    "verificar_posicao",
    "verificar_revelacao",
    "letra_para_coluna",
]

letras = "abcdefghijklmnopqrstuvwxyz"

def criar_tabuleiro(linhas, colunas):
    """Cria um tabuleiro de batalha naval com as dimensoes especificadas.

    Args:
        linhas (int): O numero de linhas do tabuleiro.
        colunas (int): O numero de colunas do tabuleiro.

    Returns:
        list: O tabuleiro criado.
    """
    tabuleiro = [['~' for _ in range(colunas)] for _ in range(linhas)]
    return tabuleiro

def letra_para_coluna(letra, colunas):
    """Converte uma letra em uma coluna do tabuleiro.
    Args:
      letra (str): A letra a ser convertida.
      colunas (int): O numero de colunas do tabuleiro.

    Returns:
      int: O indice da coluna correspondente a letra
    """
    letra = letra.strip().lower()
    if len(letra) == 1 and letra in letras[:colunas]:
        return letras.index(letra)
    return None

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro de batalha naval na tela.

    Args:
        tabuleiro (list): O tabuleiro a ser exibido.
    """
    cabecalho = letras[:len(tabuleiro[0])]
    print('    ' + '   '.join(cabecalho))
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2d}  " + '   '.join(linha))

def verificar_posicao(tabuleiro, linha, coluna):
    """Verifica se a posicao especificada no tabuleiro e valida.

    Args:
        tabuleiro (list): O tabuleiro a ser verificado.
        linha (int): A linha da posicao.
        coluna (int): A coluna da posicao.

    Returns:
        bool: True se a posicao for valida, False caso contrario.
    """
    return 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])

def verificar_revelacao(tabuleiro, linha, coluna):
    """Verifica se a posicao especificada no tabuleiro ja foi revelada.

    Args:
        tabuleiro (list): O tabuleiro a ser verificado.
        linha (int): A linha da posicao.
        coluna (int): A coluna da posicao.

    Returns:
        bool: True se a posicao ja foi revelada, False caso contrario.
    """
    return tabuleiro[linha][coluna] != '~'


