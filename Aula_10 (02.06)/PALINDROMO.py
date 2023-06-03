def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavra = input("Palavra: ")
print(palindromo(palavra))