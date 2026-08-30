def contar_ate_zero(n):
    """
    Exibe os números de n até 0, usando apenas while.
    Se o número for > 0 e divisível por 5, exibe mensagem especial.
    """
    atual = n
    while atual >= 0:
        if atual > 0 and atual % 5 == 0:
            print(f"{atual} é divisível por 5")
        else:
            print(atual)
        atual -= 1


# Programa principal
n = int(input("Digite um número inteiro maior ou igual a 0: "))
contar_ate_zero(n)