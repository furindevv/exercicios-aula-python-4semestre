def somar_multiplos(limite, divisor):
    """
    Soma todos os inteiros de 1 até limite (inclusive) que sejam
    divisíveis pelo divisor informado.
    
    Parâmetros:
        limite (int): limite superior do intervalo (>= 1)
        divisor (int): divisor a ser testado (!= 0)
    
    Retorna:
        int: soma dos múltiplos encontrados
    """
    soma = 0
    for numero in range(1, limite + 1):
        if numero % divisor == 0:
            soma += numero
    return soma


# Programa principal
limite = int(input("Digite o limite (>= 1): "))
divisor = int(input("Digite o divisor (!= 0): "))

resultado = somar_multiplos(limite, divisor)
print(f"Soma dos múltiplos de {divisor} até {limite}: {resultado}")