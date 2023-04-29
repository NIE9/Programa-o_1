def quemVenceu(numGol1, numGol2):
    if numGol1 > numGol2:
        return "1"
    elif numGol1 < numGol2:
        return "2"
    else:
        return "0"

numGol1 = int(input("Gols do time 1: "))
numGol2 = int(input("Gols do time 2: "))

#resultado = quemVenceu(numGol1, numGol2)
print(f"O resultado foi: {quemVenceu(numGol1, numGol2)}")