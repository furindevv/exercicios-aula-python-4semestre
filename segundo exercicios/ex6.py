class Pedido:
    def __init__(self, dados):
        self.dados = dados

    def calcular_total(self):
        return (
            self.dados["preco"]
            * self.dados["quantidade"]
        )


dados = {
    "produto": "Mouse",
    "quantidade": 2
}

pedido = Pedido(dados)

print(pedido.calcular_total())