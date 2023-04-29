# Exemplo de declaração de variáveis
nome = "João"
idade = 25
altura = 1.75

# Exemplo de estrutura de controle de fluxo - if/elif/else
if idade >= 18:
    print("Você é maior de idade.")
elif idade < 18:
    print("Você é menor de idade.")
else:
    print("Idade inválida.")

# Exemplo de loop - for
for i in range(1, 6):
    print(i)

# Exemplo de loop - while
x = 0
while x < 5:
    print(x)
    x += 1

#===========================================================================================================

# Exemplo de definição de função
def saudacao(nome):
    print("Olá, " + nome + "!")

# Exemplo de chamada de função
saudacao("Maria")

# Exemplo de função com retorno
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)

# Exemplo de escopo de variáveis
def exemplo_escopo():
    x = 10
    print(x)

exemplo_escopo() # imprime 10
# print(x) # Erro! x só é visível dentro da função exemplo_escopo

'''Ao definir uma função em Python, você pode usar a palavra-chave return para especificar o valor de retorno
da função, ou seja, o valor que será retornado quando a função for chamada. O return permite que a função 
calcule um valor e o retorne para ser utilizado em outras partes do código. Veja um exemplo:
'''

# Exemplo de função com retorno
def somar(a, b):
    """Função que retorna a soma de dois números."""
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado em uma variável
resultado_soma = somar(3, 5)
print(resultado_soma) # imprime 8

# Utilizando o valor de retorno em outra operação
resultado_dobro = resultado_soma * 2
print(resultado_dobro) # imprime 16

'''Neste exemplo, a função somar() recebe dois argumentos a e b, realiza a soma e armazena o resultado em 
uma variável local chamada resultado. Em seguida, a função utiliza a palavra-chave return para retornar o 
valor calculado. Ao chamar a função e passar os argumentos 3 e 5, o valor retornado é 8, que é armazenado 
em uma variável e utilizado em outras operações.

É importante notar que uma função pode ter múltiplos pontos de retorno, ou seja, diferentes trechos de 
código dentro da função podem ter instruções de return. Quando uma instrução de return é executada, a 
função retorna o valor especificado e sai da função, ignorando qualquer código subsequente. Portanto, 
é fundamental garantir que todas as possíveis rotas de execução de uma função tenham um valor de retorno 
adequado.
'''

#===========================================================================================================

'''Listas: As listas são coleções mutáveis e ordenadas de itens em Python. Você pode armazenar uma 
sequência de valores em uma lista, e acessá-los por meio de índices. Além disso, as listas podem ser 
modificadas, permitindo adicionar, remover ou modificar itens. Veja um exemplo:'''

# Exemplo de lista
frutas = ["maçã", "banana", "laranja"]
print(frutas[0]) # imprime "maçã"

# Adicionando um item à lista
frutas.append("uva")
print(frutas) # imprime ["maçã", "banana", "laranja", "uva"]

# Removendo um item da lista
frutas.remove("banana")
print(frutas) # imprime ["maçã", "laranja", "uva"]

# Modificando um item da lista
frutas[0] = "pera"
print(frutas) # imprime ["pera", "laranja", "uva"]

'''Tuplas: As tuplas são coleções imutáveis e ordenadas de itens em Python. Ou seja, uma vez que uma tupla 
é criada, seus elementos não podem ser modificados. As tuplas são geralmente utilizadas para armazenar 
conjuntos fixos de dados. Veja um exemplo:'''

# Exemplo de tupla
ponto = (3, 4)
print(ponto[0]) # imprime 3

# Tentando modificar um item da tupla (gera um erro!)
# ponto[0] = 5

# Desempacotando uma tupla
x, y = ponto
print(x, y) # imprime 3 4

'''Dicionários: Os dicionários são coleções mutáveis e não ordenadas de pares de chave-valor em Python. 
Cada valor é associado a uma chave única, permitindo o acesso rápido aos valores por meio das chaves. 
Os dicionários são úteis quando você precisa armazenar e recuperar dados com base em uma chave específica. 
Veja um exemplo:'''

# Exemplo de dicionário
pessoa = {"nome": "João", "idade": 25, "altura": 1.75}
print(pessoa["nome"]) # imprime "João"

# Exemplo de dicionário dentro de um dicionário
pessoa1 = {
    'nome': 'João',
    'idade': 30,
    'endereço': {
        'rua': 'Rua A',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'CEP': '01234-567',
    }
}
# Acessando valores em dicionários aninhados
print(pessoa1['nome']) # imprime 'João'
print(pessoa1['endereço']['cidade']) # imprime 'São Paulo'

# Adicionando um novo par chave-valor
pessoa["sexo"] = "masculino"
print(pessoa) # imprime {"nome": "João", "idade": 25, "altura": 1.75, "sexo": "masculino"}

# Removendo um par chave-valor
del pessoa["altura"]
print(pessoa) # imprime {"nome": "João", "idade": 25, "sexo": "masculino"}