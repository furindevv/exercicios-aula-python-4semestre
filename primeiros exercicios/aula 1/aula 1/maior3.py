def maior_menor():
    num1 = float(input("Me fale um numero: "))
    num2 = float(input("Me fale o segundo numero: "))
    num3 = float(input("Me fale o terceiro numero "))
    if num1 == num2 == num3 :
        print("Todas entradas sao iguais")
    else : 
        #maior
        if num1 > num2 and num1 > num3:
            maior = num1

        elif num2 > num1 and num2 > num3 :
            maior = num2

        else :
            maior = num3

        #MENOR
        
        if num1 < num2 and num1 < num3:
            menor= num1

        elif num2 < num1 and num2 < num3:
            menor = num2

        else:
            menor = num3

        print("Maior",maior)
        print("Menor", menor)

maior_menor()
              
     
    

