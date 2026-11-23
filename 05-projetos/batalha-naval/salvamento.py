__all__ = ["salvar_tabuleiro", "salvar_gabarito", "carregar_gabarito", "restaurar_tabuleiro"]

def salvar_tabuleiro(tabuleiro, nome_arquivo):
    """Salva o tabuleiro em um arquivo.

    Args:
        tabuleiro (list): O tabuleiro a ser salvo.
        nome_arquivo (str): O nome do arquivo onde o tabuleiro será salvo.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in tabuleiro:
            arquivo.write(' '.join(linha) + '\n')

def salvar_gabarito(frota_posicionada, nome_arquivo):
    """Salva as posições das embarcações em um arquivo.

    Args:
        frota_posicionada (list): Uma lista de embarcações já posicionadas.
        nome_arquivo (str): O nome do arquivo onde as posições serão salvas.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for navio in frota_posicionada:
            arquivo.write(f"{navio.nome}: {navio.posicao}\n")
def carregar_gabarito(nome_arquivo):
    """Carrega as posições das embarcações de um arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo onde as posições estão salvas.

    Returns:
        dict: Um dicionário de embarcações com suas posições carregadas.
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        gabarito = {}
        for linha in arquivo:
            if linha.strip() == "":                      # pula linha em branco
                continue
            nome, posicao_str = linha.split(':', 1)      # corta só no primeiro ':'
            texto = posicao_str.strip()[1:-1]            # tira o [ e o ] das pontas
            posicoes = []
            for par in texto.split('), ('):
                par = par.replace('(', '').replace(')', '')
                l, c = par.split(', ')
                posicoes.append((int(l), int(c)))
            gabarito[nome.strip()] = posicoes
        return gabarito

def restaurar_tabuleiro(nome_arquivo):
    """Restaura o tabuleiro a partir de um arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo onde o tabuleiro foi salvo.

    Returns:
        list: O tabuleiro restaurado.
    """

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        tabuleiro = []
        for linha in arquivo:
            if linha.strip() == "":
                continue
            tabuleiro.append(linha.strip().split())
        return tabuleiro