maior = -1
menor = 999
soma = 0

for idade in range(0, 10):
    idade = int(input("Idade: "))
    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade
    soma += idade

print(f"Maior idade: {maior}")
print(f"Menor idade: {menor}")
print(f"Média: {soma/10}")