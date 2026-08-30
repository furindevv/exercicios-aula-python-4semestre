try:
    preco = float(input("Digite um preço: "))
    print (preco)
except ValueError:
    print("Preço inválido. ")