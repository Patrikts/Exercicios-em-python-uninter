acumulador = 0

print('Seja bem-vindo a sorveteria Patrik Teixeira Saraiva')

print('********** Opções de Sorvete **********')
print('| Código |        Descrição        |  Tamanho P (500 ml)  | Tamanho M (1000 ml) | Tamanho G (2000 ml) |')
print('|   TR   |   Sabores Tradicionais  |       R$ 6,00        |       R$ 10,00      |       R$ 18,00      |')
print('|   ES   |    Sabores Especiais    |       R$ 7,00        |       R$ 12,00      |       R$ 21,00      |')
print('|   PR   |     Sabores Premium     |       R$ 8,00        |       R$ 14,00      |       R$ 24,00      |')

while True:

    tamanho = input('Entre com o TAMANHO desejado: (P/M/G) ')
    codigo = input('Entre com o CÓDIGO desejado: (TR/ES/PR) ')

    if codigo == 'TR' and tamanho == 'P':
        acumulador += 6 # acumulador guardar o valor final da conta
        print('Você pediu um sorvete sabor tradicional P de R$ 6,00')
    elif codigo == 'TR' and tamanho == 'M':
        acumulador += 10
        print('Você pediu um sorvete sabor tradicional M de R$ 10,00')
    elif codigo == 'TR' and tamanho == 'G':
        acumulador += 18
        print('Você pediu um sorvete sabor tradicional G de R$ 18,00')
    elif codigo == 'ES' and tamanho == 'P':
        acumulador += 7
        print('Você pediu um sorvete sabor especial P de R$ 7,00')
    elif codigo == 'ES' and tamanho == 'M':
        acumulador += 12
        print('Você pediu um sorvete sabor especial M de R$ 12,00')
    elif codigo == 'ES' and tamanho == 'G':
        acumulador += 21
        print('Você pediu um sorvete sabor especial G de R$ 21,00')
    elif codigo == 'PR' and tamanho == 'P':
        acumulador += 8
        print('Você pediu um sorvete sabor premium P de R$ 8,00')
    elif codigo == 'PR' and tamanho == 'M':
        acumulador += 14
        print('Você pediu um sorvete sabor premium M de R$ 14,00')
    elif codigo == 'PR' and tamanho == 'G':
        acumulador += 24
        print('Você pediu um sorvete sabor premium G de R$ 24,00')
    else:
        print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S)  !!!!!!!')
        continue
    print("O valor a ser pago está em: R$ {:.2f}".format(acumulador))
    resposta = input('Deseja pedir mais alguma coisa? (S/N): ')
    if resposta == 'S':
        continue
    else:
        print('O total a ser pago é: {:.2f}'.format(acumulador))
        break