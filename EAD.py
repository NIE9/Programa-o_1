A = input("A")
B = input("B")
oasis = 0
resultado = 0

if B.lower() == "norte":
    oasis = 0
elif B.lower() == "sul":
    oasis = 180
elif B.lower() == "leste":
    oasis = 90
elif B.lower() == "oeste":
    oasis = 270

if A.lower() == "norte":
    resultado = 0 - oasis
elif A.lower() == "sul":
    resultado = 180 - oasis
elif A.lower() == "leste":
    resultado = 90 - oasis
elif A.lower() == "oeste":
    resultado = 270 - oasis

direcao = 0
if resultado < 0:
    direcao = resultado*(-1)
    if direcao > 180:
        direcao = 360 - direcao
'''else:
    if direcao > 180:
        direcao = 360 - direcao'''

print(f"Resultado: {direcao}")