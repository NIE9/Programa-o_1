lista = []
for i in range(0, 10):
    lista.append(int(input(f"Valor {i+1}: ")))
soma=0
for j in range(len(lista)):
       soma = soma + lista[j]
media = soma / len(lista)
listaMaior = []
listaMenor = []
if lista >


'''for j in range(0, 5):
    soma = soma + lista[j]'''
'''for j in lista:
       print(j  )'''
print(soma)
print(media)