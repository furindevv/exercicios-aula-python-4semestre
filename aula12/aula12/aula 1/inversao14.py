def inverter_numero(numero):
    """
    Inverte os dígitos de um número inteiro positivo,
    usando apenas operações aritméticas (sem str, sem coleções).
    
    Parâmetros:
        numero (int): número inteiro positivo
    
    Retorna:
        int: número com os dígitos invertidos
    """
    invertido = 0
    while numero > 0:
        digito = numero % 10        # extrai o último dígito
        invertido = invertido * 10 + digito   # "empurra" o dígito para o invertido
        numero = numero // 10       # remove o último dígito do número original
    return invertido


# Programa principal
numero = int(input("Digite um número inteiro positivo: "))
resultado = inverter_numero(numero)
print(f"Número invertido: {resultado}")