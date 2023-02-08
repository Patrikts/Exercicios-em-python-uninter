A = int(input('Digite o 1ª lado do triângulo:'))
B = int(input('Digite o 2ª lado do triângulo:'))
C = int(input('Digite o 3ª lado do triângulo:'))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # se você chegou até aqui, é porque o triângulo é valido!
        if A != B and A != C and B != C:
            print('Triângulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print('Triângulo equilátero!')
            else:
                print('Triângulo isósceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')