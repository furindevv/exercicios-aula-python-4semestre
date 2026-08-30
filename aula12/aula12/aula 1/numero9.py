def eh_primo(n):
    """
    Determina se n é primo contando seus divisores positivos,
    sem usar break (percorre todo o intervalo de qualquer forma).
    
    Um número é primo se, e somente se, possui exatamente
    dois divisores positivos: 1 e ele mesmo.
    """
    quantidade_divisores = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            quantidade_divisores += 1
    
    return quantidade_divisores == 2


# Programa principal
n = int(input("Digite um número inteiro maior que 1: "))

if eh_primo(n):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")