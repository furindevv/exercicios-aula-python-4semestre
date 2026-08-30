def calcular_fatorial(n):
    """
    Calcula n! utilizando repetição, sem bibliotecas ou funções prontas.
    
    Parâmetros:
        n (int): número inteiro >= 0
    
    Retorna:
        int: fatorial de n
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Programa principal
n = int(input("Digite um número inteiro maior ou igual a 0: "))
print(f"{n}! = {calcular_fatorial(n)}")