def verificar_intervalo_paridade(numero):
    esta_no_intervalo = 10 <= numero <= 50
    par = numero % 2 == 0
    atende_ambas = esta_no_intervalo and par
    
    return esta_no_intervalo, par, atende_ambas


def exibir_resultado(numero):
    """Exibe o resultado formatado para um número."""
    esta_no_intervalo, par, atende_ambas = verificar_intervalo_paridade(numero)
    
    print(f"Está no intervalo: {esta_no_intervalo}")
    print(f"É par: {par}")
    print(f"Atende às duas regras: {atende_ambas}")


# Programa principal
numero = int(input("Digite um número inteiro: "))
exibir_resultado(numero)