class Pedido:

    def __init__(
        self,
        cliente,
        produto,
        quantidade,
        preco
    ):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def calcular_total(self):
        return self.quantidade * self.preco


pedido = Pedido(
    "Ana",
    "Mouse",
    2,
    120.0
)

print(pedido.calcular_total())