class Pedido:

    def __init__(
        self,
        identificador,
        cliente,
        produto,
        quantidade,
        preco
    ):
        self.identificador = identificador
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def calcular_total(self):
        return self.quantidade * self.preco


pedido1 = Pedido("PED-001", "Ana", "Mouse", 2, 120.0)
pedido2 = Pedido("PED-002", "Carlos", "Teclado", 1, 250.0)
pedido3 = Pedido("PED-003", "Ana", "Monitor", 1, 900.0)

pedidos = [pedido1, pedido2, pedido3]

clientes_unicos = set()

for pedido in pedidos:
    print("ID:", pedido.identificador)
    print("Cliente:", pedido.cliente)
    print("Produto:", pedido.produto)
    print("Total:", pedido.calcular_total())

    clientes_unicos.add(pedido.cliente)

print("Clientes únicos:", clientes_unicos)