import random

soma_jogador = 0
soma_mesa = 0

for x in range(2):
    carta = random.randint(1, 13)
    print(f"Carta: {carta}")
    soma_jogador = carta + soma_jogador
print(f"Sua mão é {soma_jogador}")

for x in range(2):
    carta = random.randint(1, 13)
    soma_mesa = carta + soma_mesa

while True:
    #acao = str(input("C para continuar e D para desistir: "))
    while soma_jogador <= 21:
        acao = str(input("C para continuar e D para desistir: "))
        if acao.lower() == "c":
            carta = random.randint(1,13)
            print(f"Carta: {carta}")
            soma_jogador = carta + soma_jogador
            print(f"Sua mão é {soma_jogador}")
        elif acao.lower() == "d":
            break
    print("Você perdeu!")
    break

while True:
    if soma_mesa <= 15:
        carta = random.randint(1,13)
        print(f"Carta: {carta}")
        soma_jogador = carta + soma_jogador
        print(f"Sua mão é {soma_jogador}")
    elif soma_mesa == 21 :
        break
    else:
        print(f"A mesa perdeu com: {soma_mesa}")

if soma_jogador <= 21 and soma_mesa <= 21 and soma_jogador > soma_mesa:
    print("Você venceu!")
elif soma_jogador <= 21 and soma_mesa <= 21 and soma_jogador < soma_mesa:
    print("Mesa venceu!")
elif soma_jogador > 21 and soma_mesa <= 21:
    print("Mesa venceu!")
elif soma_jogador <= 21 and soma_mesa > 21:
    print("Você venceu!")
else:
    print("Ninguém venceu!")


