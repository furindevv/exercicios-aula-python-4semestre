def classificar_numero(numero):
    """
    Classifica um número inteiro quanto ao sinal e à paridade.
    
    Parâmetros:
        numero (int): número a ser classificado
    
    Retorna:
        str: uma das strings:
             'positivo e par', 'positivo e ímpar',
             'negativo e par', 'negativo e ímpar',
             'zero'
    """
    if numero == 0:
        return "zero"
    elif numero > 0:
        if numero % 2 == 0:
            return "positivo e par"
        else:
            return "positivo e ímpar"
    else:
        if numero % 2 == 0:
            return "negativo e par"
        else:
            return "negativo e ímpar"


# Programa principal
numero = int(input("Digite um número inteiro: "))
classificacao = classificar_numero(numero)
print(classificacao)