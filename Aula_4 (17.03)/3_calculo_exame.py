def calculo(n1, n2, n3, n4):
    medFin = (n1 + n2 + n3 + n4) / 4
    if medFin >= 7:
        #print("Aprovado!")
        return "Aprovado!"
    elif medFin >= 1.7:
        #print("Exame!")
        return "Você pode fazer o exame para recuperar."
    else:
        #print("Reprovado!")
        return "Reprovado!"


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
calc = calculo(n1, n2, n3, n4)
print(calc)
