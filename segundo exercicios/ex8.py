class Pedido:

    def __init__(self, cliente, produto, quantidade, preco):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def calcular_total(self):
        return self.quantidade * self.preco


pedido1 = Pedido("Ana", "Mouse", 2, 120.0)
pedido2 = Pedido("Carlos", "Teclado", 1, 250.0)

pedidos = [pedido1, pedido2]

for pedido in pedidos:
    print("Cliente:", pedido.cliente)
    print("Produto:", pedido.produto)
    print("Total:", pedido.calcular_total())
    print()