lista = []
for i in range(0, 10):
    lista.append(int(input(f"Valor {i+1}: ")))
soma=0
for j in range(len(lista)):
       soma = soma + lista[j]
media = soma / len(lista)
listaMaior = []
listaMenor = []
for k in range(len(lista)):
    if lista[k] >= media:
        listaMaior.append(lista[k])
    else:
        listaMenor.append(lista[k])
print(f" Soma dos valores: {soma} \n Média dos valore{media} \n Valores maiores que a média: {listaMaior} \n Valores menores que a média: {listaMenor}")

'''
for j in range(0, 5):
    soma = soma + lista[j]
    
for j in lista:
   print(j)'''