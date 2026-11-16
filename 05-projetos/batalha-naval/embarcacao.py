import random

__all__ = [
    "Embarcacao",
    "frota",
    "filtrar_frota",
    "posicionar_aleatoriamente",
    "verificar_vitoria",
]

frota = {'Porta-aviões': 5, 'Encouraçado': 4, 'Cruzador': 3, 'Submarino': 3, 'Destróier': 2}
orientacoes = ['vertical', 'horizontal']
frota_posicionada = []

def filtrar_frota(frota, linhas, colunas):
    """Filtra a frota de acordo com as dimensões do tabuleiro.
    Args:
      frota (dict): A frota de embarcações.
      linhas (int): O número de linhas do tabuleiro.
      colunas (int): O número de colunas do tabuleiro.

    Returns:
      dict: Uma nova frota filtrada com base nas dimensões do tabuleiro.
    """
    frota_filtrada = {}
    for nome, tamanho in frota.items():
        if tamanho <= linhas or tamanho <= colunas:
            frota_filtrada[nome] = tamanho
    return frota_filtrada

class Embarcacao:
    """Classe que representa uma embarcação no jogo de Batalha Naval.
    Atributos:
      nome (str): O nome da embarcação.
      tamanho (int): O tamanho da embarcação.
      posicao (list): Uma lista de tuplas que representa a posição da embarcação no tabuleiro.
      acertos (list): Uma lista de tuplas que representa as posições acertadas pela embarcação.
      status (str): O status da embarcação (afundada, não atingida, atingida).
    """
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.posicao = []
        self.acertos = []
        self.status = ""

    def definir_posicao(self, linha, coluna, orientacao, linhas, colunas, frota_posicionada):
        """Define a posição da embarcação no tabuleiro.

        Args:
            linha (int): A linha da posição.
            coluna (int): A coluna da posição.
            orientacao (str): A orientação da embarcação ('horizontal' ou 'vertical').
            linhas (int): O número de linhas do tabuleiro.
            colunas (int): O número de colunas do tabuleiro.
            frota_posicionada (list): Uma lista de embarcações já posicionadas.
        Returns:
            bool: True se a posição for válida e a embarcação não colidir com outras embarcações, False caso contrário.
        """
        if orientacao not in ("horizontal", "vertical"):
            return False

        casas = []
        for i in range(self.tamanho):
            if orientacao == "horizontal":
                casas.append((linha, coluna + i))
            else:
                casas.append((linha + i, coluna))

        for l, c in casas:
            if not (0 <= l < linhas and 0 <= c < colunas):
                return False
            for navio in frota_posicionada:
                if (l, c) in navio.posicao:
                    return False

        self.posicao = casas
        return True

    def registrar_ataque(self, linha, coluna):
        """Registra um ataque na embarcação.

        Args:
            linha (int): A linha do ataque.
            coluna (int): A coluna do ataque.
        Returns:
            bool: True se o ataque foi um acerto, False caso contrário.
        """
        if (linha, coluna) in self.posicao:
            if (linha, coluna) not in self.acertos:
                self.acertos.append((linha, coluna))
                if len(self.acertos) == self.tamanho:
                    self.status = "afundada"
                return True
        return False

    def verificar_afundada(self):
        """Verifica se a embarcação foi afundada.

        Returns:
            bool: True se a embarcação foi afundada, False caso contrário.
        """
        if len(self.acertos) == self.tamanho:
            self.status = "afundada"
            return True
        return False


def verificar_vitoria(frota_posicionada):
    """Verifica se todas as embaçações foram afundadas.

    Args:
        frota_posicionada (list): Uma lista de embaçações já posicionadas.
    Returns:
        bool: True se todas as embaçações foram afundadas, False caso contrário.
    """
    for navio in frota_posicionada:
        if navio.status != "afundada":
            return False
    return True

def posicionar_aleatoriamente(nome, tamanho, linhas, colunas, frota_posicionada):
    """Posiciona uma embaçação aleatoriamente no tabuleiro.
    Args:
      nome (str): O nome da embaçação.
      tamanho (int): O tamanho da embaçação.
      linhas (int): O número de linhas do tabuleiro.
      colunas (int): O número de colunas do tabuleiro.
      frota_posicionada (list): Uma lista de embaçações já posicionadas.

    Returns:
      Embarcacao: Uma embaçação posicionada aleatoriamente no tabuleiro.
    """
    navio = Embarcacao(nome, tamanho)

    while True:
        orientacao = random.choice(["horizontal", "vertical"])
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        if navio.definir_posicao(linha, coluna, orientacao, linhas, colunas, frota_posicionada):
            return navio
        