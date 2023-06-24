import random

'''
6 | X ○ ○ ○ ○ ○ ○
5 | ○ ○ ○ ○ ○ ○ ○
4 | ○ ○ ○ ○ ○ ○ ○
3 | ○ ○ ○ ○ ○ ○ ○
2 | ○ ○ ○ ○ ○ ○ ○
1 | ○ ○ ○ ○ ○ ○ ○
    1 2  3 4  5 6 7'''

def imprime(l1, l2, l3, l4, l5, l6, linha):
    print(linha)
    print(l6)
    print(l5)
    print(l4)
    print(l3)
    print(l2)
    print(l1)
    print("=================================== \n")

def jogador1(l1, l2, l3, l4, l5, l6, entrada1):
    if entrada1 == 0:
        if l1[0] != 'X' and l1[0] != 'O':
            l1.pop(0)
            l1.insert(0, 'X')
        elif l2[0] != 'X' and l2[0] != 'O':
            l2.pop(0)
            l2.insert(0, 'X')
        elif l3[0] != 'X' and l3[0] != 'O':
            l3.pop(0)
            l3.insert(0, 'X')
        elif l4[0] != 'X' and l4[0] != 'O':
            l4.pop(0)
            l4.insert(0, 'X')
        elif l5[0] != 'X' and l5[0] != 'O':
            l5.pop(0)
            l5.insert(0, 'X')
        elif l6[0] != 'X' and l6[0] != 'O':
            l6.pop(0)
            l6.insert(0, 'X')
    elif entrada1 == 1:
        if l1[1] != 'X' and l1[1] != 'O':
            l1.pop(1)
            l1.insert(1, 'X')
        elif l2[1] != 'X' and l2[1] != 'O':
            l2.pop(1)
            l2.insert(1, 'X')
        elif l3[1] != 'X' and l3[1] != 'O':
            l3.pop(1)
            l3.insert(1, 'X')
        elif l4[1] != 'X' and l4[1] != 'O':
            l4.pop(1)
            l4.insert(1, 'X')
        elif l5[1] != 'X' and l5[1] != 'O':
            l5.pop(1)
            l5.insert(1, 'X')
        elif l6[1] != 'X' and l6[1] != 'O':
            l6.pop(1)
            l6.insert(1, 'X')
    elif entrada1 == 2:
        if l1[2] != 'X' and l1[2] != 'O':
            l1.pop(2)
            l1.insert(2, 'X')
        elif l2[2] != 'X' and l2[2] != 'O':
            l2.pop(2)
            l2.insert(2, 'X')
        elif l3[2] != 'X' and l3[2] != 'O':
            l3.pop(2)
            l3.insert(2, 'X')
        elif l4[2] != 'X' and l4[2] != 'O':
            l4.pop(2)
            l4.insert(2, 'X')
        elif l5[2] != 'X' and l5[2] != 'O':
            l5.pop(2)
            l5.insert(2, 'X')
        elif l6[2] != 'X' and l6[2] != 'O':
            l6.pop(2)
            l6.insert(2, 'X')
    elif entrada1 == 3:
        if l1[3] != 'X' and l1[3] != 'O':
            l1.pop(3)
            l1.insert(3, 'X')
        elif l2[3] != 'X' and l2[3] != 'O':
            l2.pop(3)
            l2.insert(3, 'X')
        elif l3[3] != 'X' and l3[3] != 'O':
            l3.pop(3)
            l3.insert(3, 'X')
        elif l4[3] != 'X' and l4[3] != 'O':
            l4.pop(3)
            l4.insert(3, 'X')
        elif l5[3] != 'X' and l5[3] != 'O':
            l5.pop(3)
            l5.insert(3, 'X')
        elif l6[3] != 'X' and l6[3] != 'O':
            l6.pop(3)
            l6.insert(3, 'X')
    elif entrada1 == 4:
        if l1[4] != 'X' and l1[4] != 'O':
            l1.pop(4)
            l1.insert(4, 'X')
        elif l2[4] != 'X' and l2[4] != 'O':
            l2.pop(4)
            l2.insert(4, 'X')
        elif l3[4] != 'X' and l3[4] != 'O':
            l3.pop(4)
            l3.insert(4, 'X')
        elif l4[4] != 'X' and l4[4] != 'O':
            l4.pop(4)
            l4.insert(4, 'X')
        elif l5[4] != 'X' and l5[4] != 'O':
            l5.pop(4)
            l5.insert(4, 'X')
        elif l6[4] != 'X' and l6[4] != 'O':
            l6.pop(4)
            l6.insert(4, 'X')
    elif entrada1 == 5:
        if l1[5] != 'X' and l1[5] != 'O':
            l1.pop(5)
            l1.insert(5, 'X')
        elif l2[5] != 'X' and l2[5] != 'O':
            l2.pop(5)
            l2.insert(5, 'X')
        elif l3[5] != 'X' and l3[5] != 'O':
            l3.pop(5)
            l3.insert(5, 'X')
        elif l4[5] != 'X' and l4[5] != 'O':
            l4.pop(5)
            l4.insert(5, 'X')
        elif l5[5] != 'X' and l5[5] != 'O':
            l5.pop(5)
            l5.insert(5, 'X')
        elif l6[5] != 'X' and l6[5] != 'O':
            l6.pop(5)
            l6.insert(5, 'X')
    elif entrada1 == 6:
        if l1[6] != 'X' and l1[6] != 'O':
            l1.pop(6)
            l1.insert(6, 'X')
        elif l2[6] != 'X' and l2[6] != 'O':
            l2.pop(6)
            l2.insert(6, 'X')
        elif l3[6] != 'X' and l3[6] != 'O':
            l3.pop(6)
            l3.insert(6, 'X')
        elif l4[6] != 'X' and l4[6] != 'O':
            l4.pop(6)
            l4.insert(6, 'X')
        elif l5[6] != 'X' and l5[6] != 'O':
            l5.pop(6)
            l5.insert(6, 'X')
        elif l6[6] != 'X' and l6[6] != 'O':
            l6.pop(6)
            l6.insert(6, 'X')

def jogador2(l1, l2, l3, l4, l5, l6, jogada):
    if jogada == 0:
        if l1[0] != 'X' and l1[0] != 'O':
            l1.pop(0)
            l1.insert(0, 'O')
        elif l2[0] != 'X' and l2[0] != 'O':
            l2.pop(0)
            l2.insert(0, 'O')
        elif l3[0] != 'X' and l3[0] != 'O':
            l3.pop(0)
            l3.insert(0, 'O')
        elif l4[0] != 'X' and l4[0] != 'O':
            l4.pop(0)
            l4.insert(0, 'O')
        elif l5[0] != 'X' and l5[0] != 'O':
            l5.pop(0)
            l5.insert(0, 'O')
        elif l6[0] != 'X' and l6[0] != 'O':
            l6.pop(0)
            l6.insert(0, 'O')
    elif jogada == 1:
        if l1[1] != 'X' and l1[1] != 'O':
            l1.pop(1)
            l1.insert(1, 'O')
        elif l2[1] != 'X' and l2[1] != 'O':
            l2.pop(1)
            l2.insert(1, 'O')
        elif l3[1] != 'X' and l3[1] != 'O':
            l3.pop(1)
            l3.insert(1, 'O')
        elif l4[1] != 'X' and l4[1] != 'O':
            l4.pop(1)
            l4.insert(1, 'O')
        elif l5[1] != 'X' and l5[1] != 'O':
            l5.pop(1)
            l5.insert(1, 'O')
        elif l6[1] != 'X' and l6[1] != 'O':
            l6.pop(1)
            l6.insert(1, 'O')
    elif jogada == 2:
        if l1[2] != 'X' and l1[2] != 'O':
            l1.pop(2)
            l1.insert(2, 'O')
        elif l2[2] != 'X' and l2[2] != 'O':
            l2.pop(2)
            l2.insert(2, 'O')
        elif l3[2] != 'X' and l3[2] != 'O':
            l3.pop(2)
            l3.insert(2, 'O')
        elif l4[2] != 'X' and l4[2] != 'O':
            l4.pop(2)
            l4.insert(2, 'O')
        elif l5[2] != 'X' and l5[2] != 'O':
            l5.pop(2)
            l5.insert(2, 'O')
        elif l6[2] != 'X' and l6[2] != 'O':
            l6.pop(2)
            l6.insert(2, 'O')
    elif jogada == 3:
        if l1[3] != 'X' and l1[3] != 'O':
            l1.pop(3)
            l1.insert(3, 'O')
        elif l2[3] != 'X' and l2[3] != 'O':
            l2.pop(3)
            l2.insert(3, 'O')
        elif l3[3] != 'X' and l3[3] != 'O':
            l3.pop(3)
            l3.insert(3, 'O')
        elif l4[3] != 'X' and l4[3] != 'O':
            l4.pop(3)
            l4.insert(3, 'O')
        elif l5[3] != 'X' and l5[3] != 'O':
            l5.pop(3)
            l5.insert(3, 'O')
        elif l6[3] != 'X' and l6[3] != 'O':
            l6.pop(3)
            l6.insert(3, 'O')
    elif jogada == 4:
        if l1[4] != 'X' and l1[4] != 'O':
            l1.pop(4)
            l1.insert(4, 'O')
        elif l2[4] != 'X' and l2[4] != 'O':
            l2.pop(4)
            l2.insert(4, 'O')
        elif l3[4] != 'X' and l3[4] != 'O':
            l3.pop(4)
            l3.insert(4, 'O')
        elif l4[4] != 'X' and l4[4] != 'O':
            l4.pop(4)
            l4.insert(4, 'O')
        elif l5[4] != 'X' and l5[4] != 'O':
            l5.pop(4)
            l5.insert(4, 'O')
        elif l6[4] != 'X' and l6[4] != 'O':
            l6.pop(4)
            l6.insert(4, 'O')
    elif jogada == 5:
        if l1[5] != 'X' and l1[5] != 'O':
            l1.pop(5)
            l1.insert(5, 'O')
        elif l2[5] != 'X' and l2[5] != 'O':
            l2.pop(5)
            l2.insert(5, 'O')
        elif l3[5] != 'X' and l3[5] != 'O':
            l3.pop(5)
            l3.insert(5, 'O')
        elif l4[5] != 'X' and l4[5] != 'O':
            l4.pop(5)
            l4.insert(5, 'O')
        elif l5[5] != 'X' and l5[5] != 'O':
            l5.pop(5)
            l5.insert(5, 'O')
        elif l6[5] != 'X' and l6[5] != 'O':
            l6.pop(5)
            l6.insert(5, 'O')
    elif jogada == 6:
        if l1[6] != 'X' and l1[6] != 'O':
            l1.pop(6)
            l1.insert(6, 'O')
        elif l2[6] != 'X' and l2[6] != 'O':
            l2.pop(6)
            l2.insert(6, 'O')
        elif l3[6] != 'X' and l3[6] != 'O':
            l3.pop(6)
            l3.insert(6, 'O')
        elif l4[6] != 'X' and l4[6] != 'O':
            l4.pop(6)
            l4.insert(6, 'O')
        elif l5[6] != 'X' and l5[6] != 'O':
            l5.pop(6)
            l5.insert(6, 'O')
        elif l6[6] != 'X' and l6[6] != 'O':
            l6.pop(6)
            l6.insert(6, 'O')

def verificarX(l1, l2, l3, l4, l5, l6):
    vitoriaX = "Vitória do jogador 1!"
    if l1[0:4].count("X") == 4:
        return vitoriaX
    elif l1[1:5].count("X") == 4:
        return vitoriaX
    elif l1[2:6].count("X") == 4:
        return vitoriaX
    elif l1[3:7].count("X") == 4:
        return vitoriaX
    elif l2[0:4].count("X") == 4:
        return vitoriaX
    elif l2[1:5].count("X") == 4:
        return vitoriaX
    elif l2[2:6].count("X") == 4:
        return vitoriaX
    elif l2[3:7].count("X") == 4:
        return vitoriaX
    elif l3[0:4].count("X") == 4:
        return vitoriaX
    elif l3[1:5].count("X") == 4:
        return vitoriaX
    elif l3[2:6].count("X") == 4:
        return vitoriaX
    elif l3[3:7].count("X") == 4:
        return vitoriaX
    elif l4[0:4].count("X") == 4:
        return vitoriaX
    elif l4[1:5].count("X") == 4:
        return vitoriaX
    elif l4[2:6].count("X") == 4:
        return vitoriaX
    elif l4[3:7].count("X") == 4:
        return vitoriaX
    elif l5[0:4].count("X") == 4:
        return vitoriaX
    elif l5[1:5].count("X") == 4:
        return vitoriaX
    elif l5[2:6].count("X") == 4:
        return vitoriaX
    elif l5[3:7].count("X") == 4:
        return vitoriaX
    elif l6[0:4].count("X") == 4:
        return vitoriaX
    elif l6[1:5].count("X") == 4:
        return vitoriaX
    elif l6[2:6].count("X") == 4:
        return vitoriaX
    elif l6[3:7].count("X") == 4:
        return vitoriaX
    elif l1[0] == 'X' and l2[0] == 'X' and l3[0] == 'X' and l4[0] == 'X':
        return vitoriaX
    elif l2[0] == 'X' and l3[0] == 'X' and l4[0] == 'X' and l5[0] == 'X':
        return vitoriaX
    elif l3[0] == 'X' and l4[0] == 'X' and l5[0] == 'X' and l6[0] == 'X':
        return vitoriaX
    elif l1[1] == 'X' and l2[1] == 'X' and l3[1] == 'X' and l4[1] == 'X':
        return vitoriaX
    elif l2[1] == 'X' and l3[1] == 'X' and l4[1] == 'X' and l5[1] == 'X':
        return vitoriaX
    elif l3[1] == 'X' and l4[1] == 'X' and l5[1] == 'X' and l6[1] == 'X':
        return vitoriaX
    elif l1[2] == 'X' and l2[2] == 'X' and l3[2] == 'X' and l4[2] == 'X':
        return vitoriaX
    elif l2[2] == 'X' and l3[2] == 'X' and l4[2] == 'X' and l5[2] == 'X':
        return vitoriaX
    elif l3[2] == 'X' and l4[2] == 'X' and l5[2] == 'X' and l6[2] == 'X':
        return vitoriaX
    elif l1[3] == 'X' and l2[3] == 'X' and l3[3] == 'X' and l4[3] == 'X':
        return vitoriaX
    elif l2[3] == 'X' and l3[3] == 'X' and l4[3] == 'X' and l5[3] == 'X':
        return vitoriaX
    elif l3[3] == 'X' and l4[3] == 'X' and l5[3] == 'X' and l6[3] == 'X':
        return vitoriaX
    elif l1[4] == 'X' and l2[4] == 'X' and l3[4] == 'X' and l4[4] == 'X':
        return vitoriaX
    elif l2[4] == 'X' and l3[4] == 'X' and l4[4] == 'X' and l5[4] == 'X':
        return vitoriaX
    elif l3[4] == 'X' and l4[4] == 'X' and l5[4] == 'X' and l6[4] == 'X':
        return vitoriaX
    elif l1[5] == 'X' and l2[5] == 'X' and l3[5] == 'X' and l4[5] == 'X':
        return vitoriaX
    elif l2[5] == 'X' and l3[5] == 'X' and l4[5] == 'X' and l5[5] == 'X':
        return vitoriaX
    elif l3[5] == 'X' and l4[5] == 'X' and l5[5] == 'X' and l6[5] == 'X':
        return vitoriaX
    elif l1[6] == 'X' and l2[6] == 'X' and l3[6] == 'X' and l4[6] == 'X':
        return vitoriaX
    elif l2[6] == 'X' and l3[6] == 'X' and l4[6] == 'X' and l5[6] == 'X':
        return vitoriaX
    elif l3[6] == 'X' and l4[6] == 'X' and l5[6] == 'X' and l6[6] == 'X':
        return vitoriaX

    elif l1[0] == 'X' and l2[1] == 'X' and l3[2] == 'X' and l4[3] == 'X':
        return vitoriaX
    elif l1[1] == 'X' and l2[2] == 'X' and l3[3] == 'X' and l4[4] == 'X':
        return vitoriaX
    elif l1[2] == 'X' and l2[3] == 'X' and l3[4] == 'X' and l4[5] == 'X':
        return vitoriaX
    elif l1[3] == 'X' and l2[4] == 'X' and l3[5] == 'X' and l4[6] == 'X':
        return vitoriaX
    elif l2[0] == 'X' and l3[1] == 'X' and l4[2] == 'X' and l5[3] == 'X':
        return vitoriaX
    elif l2[1] == 'X' and l3[2] == 'X' and l4[3] == 'X' and l5[4] == 'X':
        return vitoriaX
    elif l2[2] == 'X' and l3[3] == 'X' and l4[4] == 'X' and l5[5] == 'X':
        return vitoriaX
    elif l2[3] == 'X' and l3[4] == 'X' and l4[5] == 'X' and l5[6] == 'X':
        return vitoriaX
    elif l3[0] == 'X' and l4[1] == 'X' and l5[2] == 'X' and l6[3] == 'X':
        return vitoriaX
    elif l3[1] == 'X' and l4[2] == 'X' and l5[3] == 'X' and l6[4] == 'X':
        return vitoriaX
    elif l3[2] == 'X' and l4[3] == 'X' and l5[4] == 'X' and l6[5] == 'X':
        return vitoriaX
    elif l3[3] == 'X' and l4[4] == 'X' and l5[5] == 'X' and l6[6] == 'X':
        return vitoriaX
    elif l6[0] == 'X' and l5[1] == 'X' and l4[2] == 'X' and l3[3] == 'X':
        return vitoriaX
    elif l6[1] == 'X' and l5[2] == 'X' and l4[3] == 'X' and l3[4] == 'X':
        return vitoriaX
    elif l6[2] == 'X' and l5[3] == 'X' and l4[4] == 'X' and l3[5] == 'X':
        return vitoriaX
    elif l6[3] == 'X' and l5[4] == 'X' and l4[5] == 'X' and l3[6] == 'X':
        return vitoriaX
    elif l5[0] == 'X' and l4[1] == 'X' and l3[2] == 'X' and l2[3] == 'X':
        return vitoriaX
    elif l5[1] == 'X' and l4[2] == 'X' and l3[3] == 'X' and l2[4] == 'X':
        return vitoriaX
    elif l5[2] == 'X' and l4[3] == 'X' and l3[4] == 'X' and l2[5] == 'X':
        return vitoriaX
    elif l5[3] == 'X' and l4[4] == 'X' and l3[5] == 'X' and l2[6] == 'X':
        return vitoriaX
    elif l4[0] == 'X' and l3[1] == 'X' and l2[2] == 'X' and l1[3] == 'X':
        return vitoriaX
    elif l4[1] == 'X' and l3[2] == 'X' and l2[3] == 'X' and l1[4] == 'X':
        return vitoriaX
    elif l4[2] == 'X' and l3[3] == 'X' and l2[4] == 'X' and l1[5] == 'X':
        return vitoriaX
    elif l4[3] == 'X' and l3[4] == 'X' and l2[5] == 'X' and l1[6] == 'X':
        return vitoriaX

def verificarO(l1, l2, l3, l4, l5, l6):
    vitoriaO = "Vitória do jogador 2!"
    if l1[0:4].count("O") == 4:
        return vitoriaO
    elif l1[1:5].count("O") == 4:
        return vitoriaO
    elif l1[2:6].count("O") == 4:
        return vitoriaO
    elif l1[3:7].count("O") == 4:
        return vitoriaO
    elif l2[0:4].count("O") == 4:
        return vitoriaO
    elif l2[1:5].count("O") == 4:
        return vitoriaO
    elif l2[2:6].count("O") == 4:
        return vitoriaO
    elif l2[3:7].count("O") == 4:
        return vitoriaO
    elif l3[0:4].count("O") == 4:
        return vitoriaO
    elif l3[1:5].count("O") == 4:
        return vitoriaO
    elif l3[2:6].count("O") == 4:
        return vitoriaO
    elif l3[3:7].count("O") == 4:
        return vitoriaO
    elif l4[0:4].count("O") == 4:
        return vitoriaO
    elif l4[1:5].count("O") == 4:
        return vitoriaO
    elif l4[2:6].count("O") == 4:
        return vitoriaO
    elif l4[3:7].count("O") == 4:
        return vitoriaO
    elif l5[0:4].count("O") == 4:
        return vitoriaO
    elif l5[1:5].count("O") == 4:
        return vitoriaO
    elif l5[2:6].count("O") == 4:
        return vitoriaO
    elif l5[3:7].count("O") == 4:
        return vitoriaO
    elif l6[0:4].count("O") == 4:
        return vitoriaO
    elif l6[1:5].count("O") == 4:
        return vitoriaO
    elif l6[2:6].count("O") == 4:
        return vitoriaO
    elif l6[3:7].count("O") == 4:
        return vitoriaO
    elif l1[0] == 'O' and l2[0] == 'O' and l3[0] == 'O' and l4[0] == 'O':
        return vitoriaO
    elif l2[0] == 'O' and l3[0] == 'O' and l4[0] == 'O' and l5[0] == 'O':
        return vitoriaO
    elif l3[0] == 'O' and l4[0] == 'O' and l5[0] == 'O' and l6[0] == 'O':
        return vitoriaO
    elif l1[1] == 'O' and l2[1] == 'O' and l3[1] == 'O' and l4[1] == 'O':
        return vitoriaO
    elif l2[1] == 'O' and l3[1] == 'O' and l4[1] == 'O' and l5[1] == 'O':
        return vitoriaO
    elif l3[1] == 'O' and l4[1] == 'O' and l5[1] == 'O' and l6[1] == 'O':
        return vitoriaO
    elif l1[2] == 'O' and l2[2] == 'O' and l3[2] == 'O' and l4[2] == 'O':
        return vitoriaO
    elif l2[2] == 'O' and l3[2] == 'O' and l4[2] == 'O' and l5[2] == 'O':
        return vitoriaO
    elif l3[2] == 'O' and l4[2] == 'O' and l5[2] == 'O' and l6[2] == 'O':
        return vitoriaO
    elif l1[3] == 'O' and l2[3] == 'O' and l3[3] == 'O' and l4[3] == 'O':
        return vitoriaO
    elif l2[3] == 'O' and l3[3] == 'O' and l4[3] == 'O' and l5[3] == 'O':
        return vitoriaO
    elif l3[3] == 'O' and l4[3] == 'O' and l5[3] == 'O' and l6[3] == '0':
        return vitoriaO
    elif l1[4] == 'O' and l2[4] == 'O' and l3[4] == 'O' and l4[4] == 'O':
        return vitoriaO
    elif l2[4] == 'O' and l3[4] == 'O' and l4[4] == 'O' and l5[4] == 'O':
        return vitoriaO
    elif l3[4] == 'O' and l4[4] == 'O' and l5[4] == 'O' and l6[4] == 'O':
        return vitoriaO
    elif l1[5] == 'O' and l2[5] == 'O' and l3[5] == 'O' and l4[5] == 'O':
        return vitoriaO
    elif l2[5] == 'O' and l3[5] == 'O' and l4[5] == 'O' and l5[5] == 'O':
        return vitoriaO
    elif l3[5] == 'O' and l4[5] == 'O' and l5[5] == 'O' and l6[5] == 'O':
        return vitoriaO
    elif l1[6] == 'O' and l2[6] == 'O' and l3[6] == 'O' and l4[6] == 'O':
        return vitoriaO
    elif l2[6] == 'O' and l3[6] == 'O' and l4[6] == 'O' and l5[6] == 'O':
        return vitoriaO
    elif l3[6] == 'O' and l4[6] == 'O' and l5[6] == 'O' and l6[6] == 'O':
        return vitoriaO

    elif l1[0] == 'O' and l2[1] == 'O' and l3[2] == 'O' and l4[3] == 'O':
        return vitoriaO
    elif l1[1] == 'O' and l2[2] == 'O' and l3[3] == 'O' and l4[4] == 'O':
        return vitoriaO
    elif l1[2] == 'O' and l2[3] == 'O' and l3[4] == 'O' and l4[5] == 'O':
        return vitoriaO
    elif l1[3] == 'O' and l2[4] == 'O' and l3[5] == 'O' and l4[6] == 'O':
        return vitoriaO
    elif l2[0] == 'O' and l3[1] == 'O' and l4[2] == 'O' and l5[3] == 'O':
        return vitoriaO
    elif l2[1] == 'O' and l3[2] == 'O' and l4[3] == 'O' and l5[4] == 'O':
        return vitoriaO
    elif l2[2] == 'O' and l3[3] == 'O' and l4[4] == 'O' and l5[5] == 'O':
        return vitoriaO
    elif l2[3] == 'O' and l3[4] == 'O' and l4[5] == 'O' and l5[6] == 'O':
        return vitoriaO
    elif l3[0] == 'O' and l4[1] == 'O' and l5[2] == 'O' and l6[3] == 'O':
        return vitoriaO
    elif l3[1] == 'O' and l4[2] == 'O' and l5[3] == 'O' and l6[4] == 'O':
        return vitoriaO
    elif l3[2] == 'O' and l4[3] == 'O' and l5[4] == 'O' and l6[5] == 'O':
        return vitoriaO
    elif l3[3] == 'O' and l4[4] == 'O' and l5[5] == 'O' and l6[6] == 'O':
        return vitoriaO
    elif l6[0] == 'O' and l5[1] == 'O' and l4[2] == 'O' and l3[3] == 'O':
        return vitoriaO
    elif l6[1] == 'O' and l5[2] == 'O' and l4[3] == 'O' and l3[4] == 'O':
        return vitoriaO
    elif l6[2] == 'O' and l5[3] == 'O' and l4[4] == 'O' and l3[5] == 'O':
        return vitoriaO
    elif l6[3] == 'O' and l5[4] == 'O' and l4[5] == 'O' and l3[6] == 'O':
        return vitoriaO
    elif l5[0] == 'O' and l4[1] == 'O' and l3[2] == 'O' and l2[3] == 'O':
        return vitoriaO
    elif l5[1] == 'O' and l4[2] == 'O' and l3[3] == 'O' and l2[4] == 'O':
        return vitoriaO
    elif l5[2] == 'O' and l4[3] == 'O' and l3[4] == 'O' and l2[5] == 'O':
        return vitoriaO
    elif l5[3] == 'O' and l4[4] == 'O' and l3[5] == 'O' and l2[6] == 'O':
        return vitoriaO
    elif l4[0] == 'O' and l3[1] == 'O' and l2[2] == 'O' and l1[3] == 'O':
        return vitoriaO
    elif l4[1] == 'O' and l3[2] == 'O' and l2[3] == 'O' and l1[4] == 'O':
        return vitoriaO
    elif l4[2] == 'O' and l3[3] == 'O' and l2[4] == 'O' and l1[5] == 'O':
        return vitoriaO
    elif l4[3] == 'O' and l3[4] == 'O' and l2[5] == 'O' and l1[6] == 'O':
        return vitoriaO

linha = ['0', '1', '2', '3', '4', '5', '6']
l6 = ['_', '_', '_', '_', '_', '_', '_']
l5 = ['_', '_', '_', '_', '_', '_', '_']
l4 = ['_', '_', '_', '_', '_', '_', '_']
l3 = ['_', '_', '_', '_', '_', '_', '_']
l2 = ['_', '_', '_', '_', '_', '_', '_']
l1 = ['_', '_', '_', '_', '_', '_', '_']

escolha = str(input("Dois jogadores? (sim/não): "))
imprime(l1, l2, l3, l4, l5, l6, linha)
while True:
    entrada1 = int(input("Jogador 1: "))
    jogador1(l1, l2, l3, l4, l5, l6, entrada1)
    veri1 = verificarX(l1, l2, l3, l4, l5, l6)
    verificarX(l1, l2, l3, l4, l5, l6)
    imprime(l1, l2, l3, l4, l5, l6, linha)
    if veri1 == "Vitória do jogador 1!":
        print(veri1)
        break
    elif (l6[0:7].count('X') + l6[0:7].count('O')) == 7:
        print("Empatou!")
        break

    if escolha.lower() == "não":
        jogada = random.randint(0,6)
        print(f"Computador: {jogada} \n")
        jogador2(l1, l2, l3, l4, l5, l6, jogada)
        imprime(l1, l2, l3, l4, l5, l6, linha)
    elif escolha.lower() == "sim":
        jogada = int(input("Jogador 2: "))
        jogador2(l1, l2, l3, l4, l5, l6, jogada)
        imprime(l1, l2, l3, l4, l5, l6, linha)

    veri2 = verificarO(l1, l2, l3, l4, l5, l6)
    verificarO(l1, l2, l3, l4, l5, l6)
    imprime(l1, l2, l3, l4, l5, l6, linha)
    if veri2 == "Vitória do jogador 2!":
        if escolha.lower() == "não":
            print("Vitória do computador!")
        elif escolha.lower() == "sim":
            print("Vitória do jogador 2!")
        break
    elif (l6[0:7].count('X') + l6[0:7].count('O')) == 7:
        print("Empatou!")
        break
    else:
        continue






