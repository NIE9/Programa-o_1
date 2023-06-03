lista1 = []
total = 0
while True:
    entrada = int(input("Qual o melhor Sistema Operacional para uso em servidores?:"))
    if entrada not in range(0,6):
        continue
    elif entrada in range(1,6):
        lista1.append(entrada)
        total += 1
    elif entrada == 0:
        break

resultado = {'Windows_Server' : {'quantidade' : lista1.count(1), 'porcentagem': str(int((100/total) * lista1.count(1)))+"%"}, 'Unix' : {'quantidade' : lista1.count(2), 'porcentagem': str(int((100/total) * lista1.count(2)))+"%"}, 'Linux' : {'quantidade' : lista1.count(3), 'porcentagem': str(int((100/total) * lista1.count(3)))+"%"}, 'Netware' : {'quantidade' : lista1.count(4), 'porcentagem': str(int((100/total) * lista1.count(4)))+"%"}, 'Mac_OS' : {'quantidade' : lista1.count(5), 'porcentagem': str(int((100/total) * lista1.count(5)))+"%"}, 'Outro' : {'quantidade' : lista1.count(6), 'porcentagem': str(int((100/total) * lista1.count(6)))+"%"}}

print(resultado)

"""Windows_Server = lista1.count(1)
Unix = lista1.count(2)
Linux = lista1.count(3)
Netware = lista1.count(4)
Mac_OS = lista1.count(5)
Outro = lista1.count(6)"""