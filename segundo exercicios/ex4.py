pedidos = [
    {
        "id": "PED-001",
        "cliente": "Ana",
        "produto": "Mouse",
        "quantidade": 2,
        "preco": 120.0
    },
    {
        "id": "PED-002",
        "cliente": "Carlos",
        "produto": "Teclado",
        "quantidade": 1,
        "preco": 250.0
    },
    {
        "id": "PED-003",
        "cliente": "Ana",
        "produto": "Monitor",
        "quantidade": 1,
        "preco": 900.0
    }
]
for pedido in pedidos: 
    print (pedido)

for pedido in pedidos:
    print(
        pedido["cliente"],
        "-",
        pedido["produto"]
    )
clientes_unicos = set()

clientes_unicos.add ("augusto")

print(clientes_unicos)