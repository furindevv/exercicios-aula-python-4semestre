def calcular(a, b, operacao):
    """
    Realiza uma operação aritmética entre a e b.
    
    Parâmetros:
        a (int/float): primeiro operando
        b (int/float): segundo operando
        operacao (str): um dos símbolos '+', '-', '*', '/'
    
    Retorna:
        int/float: resultado da operação, ou
        None: se a operação for inválida ou houver divisão por zero
    """
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None


# Programa principal
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = calcular(a, b, operacao)

if resultado is None:
    print("Operação inválida")
else:
    print(resultado)