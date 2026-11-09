def fatorial(n):
    """Calcula o fatorial de um número inteiro não negativo.
    Args:
        n (int): O número para calcular o fatorial.
    Returns:
        int: O fatorial do número.
    """
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
try:
    resultado = fatorial(n)
    print(f"O fatorial de {n} é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
