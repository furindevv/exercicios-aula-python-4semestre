def media_aluno():
    nota1 = float(input("digite sua nota "))
    nota2 = float(input("digite sua nota "))
    nota3 = float(input("digite sua nota "))
    media = ( nota1+nota2+nota3) / 3

    if media < 4:
        print (f"Voce esta Reprovado {media:.2f}")
    elif media >= 4 and media < 6:
        print (f"Voce esta de recuperação {media:.2f}")
    elif media >=6 and media < 9:
        print (f"Voce esta aprovado {media:.2f}")
    elif  media >= 9:
        print (f"Voce esta aprovado com destaque maximo {media:.2f}")
    
media_aluno()


