def potencia(base, expoente):
    """
    Calcula base^expoente usando multiplicações sucessivas,
    sem usar o operador ** ou bibliotecas.
    
    Parâmetros:
        base (int/float): a base da potência
        expoente (int): expoente inteiro >= 0
    
    Retorna:
        int/float: resultado de base elevado a expoente
    """
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


# Programa principal
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente (>= 0): "))

resultado = potencia(base, expoente)
print(f"{base} ^ {expoente} = {resultado}")
