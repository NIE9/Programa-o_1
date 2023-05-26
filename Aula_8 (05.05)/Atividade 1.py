
contador = 0
nota = float(0)

while True:
    entrada = input(f"Digite a nota {contador+1}:")
    if entrada == "sair":
        break
    elif entrada.strip() == "":
        nota = nota
    else:
        entrada_int = float(entrada)
        contador += 1
        nota = (nota + entrada_int)
media = nota/contador
print(f"A média do aluno é {media}")


