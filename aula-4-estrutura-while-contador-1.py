inicial = int(input('Qual valor deseja iniciar a contagem?'))
final = int(input('Qual valor dejesa encerrar a contagem?'))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1
# conta os numeros pares