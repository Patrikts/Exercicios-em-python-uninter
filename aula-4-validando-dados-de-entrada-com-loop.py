# validando a entrada
x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...'.format(x))