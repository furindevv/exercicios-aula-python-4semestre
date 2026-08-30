cliente = {
    "nome" : "Ana",
    "email" : "ana@gmail.com",
    "idade" : 24       
           }

print (cliente["nome"])

cliente ["cidade"] = "sao paulo"
print(cliente)

cliente["idade"] = 25
print(cliente)

del cliente ["cidade"]
print (cliente)
