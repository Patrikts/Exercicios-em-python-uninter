km = int(input('Quantos km foram percorridos?'))
dias = int(input('Por quantos dias ele foi alugado?'))

preco = 60 * dias + 0.15 * km
print('km = {}. Dias: {}'.format(km, dias))
print('Valor a ser pago: {}'.format(preco))
