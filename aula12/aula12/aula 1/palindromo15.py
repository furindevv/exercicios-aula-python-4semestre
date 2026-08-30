def eh_palindromo(numero):
    """
    Verifica se um número inteiro positivo é palíndromo,
    construindo numericamente seu inverso (sem str, sem coleções).
    
    Parâmetros:
        numero (int): número inteiro positivo
    
    Retorna:
        bool: True se for palíndromo, False caso contrário
    """
    original = numero      # preserva o valor original
    invertido = 0
    
    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10
    
    return invertido == original


# Programa principal
numero = int(input("Digite um número inteiro positivo: "))

if eh_palindromo(numero):
    print("Palíndromo")
else:
    print("Não palíndromo")