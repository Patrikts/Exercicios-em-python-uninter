soma = 0
cont = 1
while (cont <= 5):
    x = int(input('Digite o {}ª número:'.format(cont)))
    soma += x # Equivalente: soma = soma + x
    cont += 1 # Equivalente: cont = cont + 1
print('Somatório: {}'.format(soma))