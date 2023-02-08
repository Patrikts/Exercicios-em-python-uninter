acumulador = 0

print('********** Opções de Serviço **********')
print('| Código |      Descrição     |  Valor  | ')
print('|   cc   |   Corte de Cabelo  |  80,00  | ')
print('|   pe   | Penteado Elaborado | 220,00  | ')
print('|   pi   |       Pintura      | 120,00  |')
print('|   pr   |     Progressiva    | 450,00  |')
print('|   es   |       Escova       | 100,00  |')
print('Seja bem-vindo ao salão de beleza Patrik Teixeira Saraiva')

while True:
    codigo = input('Entre com o código desejado: ')
    if codigo == 'cc':
        acumulador += 80 # acumulador guardar o valor final de serviços
    elif codigo == 'pe':
        acumulador += 220
    elif codigo == 'pi':
        acumulador += 120
    elif codigo == 'pr':
        acumulador += 450
    elif codigo == 'es':
        acumulador += 100
    else:
        print('Pare de digitar caracteres errados')
        continue
    print("O valor a ser pago está em: {:.2f}".format(acumulador))
    resposta = input('Deseja mais algum serviço (s/n?')
    if resposta == 's':
        continue
    else:
        print('O valor final da conta é: {:.2f}'.format(acumulador))
        break









