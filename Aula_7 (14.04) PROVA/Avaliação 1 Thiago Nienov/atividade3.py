def ingresso(amiga1, amiga2):
    a1 = 0
    a2 = 0
    while True:
        if amiga1 <= 17:
            a1 = 15
        elif amiga1 <= 59:
            a1 = 30
        else:
            a1 = 20

        if amiga2 <= 17:
            a2 = 15
            break
        elif amiga2 <= 59:
            a2 = 30
            break
        else:
            a2 = 20
            break

    total = a1 + a2
    return total

amiga1 = int(input("Idade da amiga 1: "))
amiga2 = int(input("Idade da amiga 2: "))
tot = ingresso(amiga1, amiga2)
print(tot)
