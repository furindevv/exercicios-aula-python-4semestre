def gerar_sequencia(inicio, passo, quantidade):
    """
    Exibe 'quantidade' valores de uma sequência aritmética,
    começando em 'inicio' e incrementando 'passo' a cada termo.
    
    Não armazena os valores em nenhuma coleção — cada termo é
    calculado e exibido no momento em que é gerado.
    """
    valor_atual = inicio
    resultado = ""
    
    for i in range(quantidade):
        if i == 0:
            resultado += str(valor_atual)
        else:
            resultado += ", " + str(valor_atual)
        valor_atual += passo
    
    print(resultado)


# Programa principal
inicio = int(input("Digite o valor inicial: "))
passo = int(input("Digite o passo: "))
quantidade = int(input("Digite a quantidade de valores (>= 1): "))

gerar_sequencia(inicio, passo, quantidade)
