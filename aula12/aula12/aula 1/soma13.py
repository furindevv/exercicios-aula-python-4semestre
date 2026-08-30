def somar_digitos(numero):
    """
    Calcula a soma dos dígitos de um número inteiro positivo,
    usando apenas operações aritméticas (sem str, sem coleções).
    
    Parâmetros:
        numero (int): número inteiro positivo
    
    Retorna:
        int: soma dos dígitos
    """
    soma = 0
    while numero > 0:
        digito = numero % 10      # extrai o último dígito
        soma += digito
        numero = numero // 10     # remove o último dígito
    return soma


# Programa principal
numero = int(input("Digite um número inteiro positivo: "))
resultado = somar_digitos(numero)
print(f"Soma dos dígitos: {resultado}")