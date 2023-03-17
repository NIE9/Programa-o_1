import random

numOculto = random.randint(0, 10)
while True:
    numEscolhido = int(input("Número aleatório: "))
    if numEscolhido == numOculto:
        print("Acertou!")
        break
    elif numEscolhido > numOculto:
        print("Um pouquinho menos!\n")
    else:
        print("Um pouquinho mais!\n")
