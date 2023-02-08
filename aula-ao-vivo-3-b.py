#Exercício 3 de 4 da atividade prática

#Início da função volumeFeijoada ()
def volumeFeijoada():
    print('---------- Menu 1 de 3 - Volume Feijoada ----------')
    while True:
        try:
            volumeF = int(input('Digite a quantidade desejada (ml): \n' + '>> '))
            if (volumeF >= 300) and (volumeF <= 5000): #if 300 <= volumeF <= 5000:
                return volumeF * 0.08
            else:
                print('Pare de digitar valores abaixo de 300 ou acima de 5000.')
                continue # retorna para o inicio do laço (retorna para pergunta)
        except ValueError: # Caso o usuário digite valores double ou string e não inteiros
            print('Pare de digitar valores não inteiros!')

#Fim da função volumeFeijoada ()

#Início da função opcaoFeijoada ()
def opcaoFeijoada():
    print('---------- Menu 2 de 3 - Opção Feijoada ----------')
    while True:
        opcaoF = input('Qual opção de feijoada deseja \n' +
                       'b - Básica (Feijão + paiol + costelinha) \n' +
                       'p - Premium (Feijão + paiol + costelinha + partes de porco) \n' +
                       's - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n' +
                       '>> ')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Pare de digitar opções diferentes de b/p/s!')
            continue # retorna para inicio do laço (retorna para pergunta)
#Fim da função opcaoFeijoada()

#Início da função acompanhamentoFeijoada ()
def acompanhamentoFeijoada():
    print('---------- Menu 3 de 3 - Acompanhamento Feijoada ----------')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja mais algum adicional: \n' +
                                '0 - Não desejo mais acompanhamentos (encerrar pedido) \n' +
                                '1 - 200g de arroz \n' +
                                '2 - 150g de farofa especial \n' +
                                '3 - 100g de couve cozida \n' +
                                '4 - 1 laranja descascada \n' +
                                '>> ')
        if acompanhamentoF == '0':
            return acumulador
        elif acompanhamentoF == '1':
            acumulador += 5
            continue # volta para o inicio do while True
        elif acompanhamentoF == '2':
            acumulador += 6
            continue # volta para o inicio do while True
        elif acompanhamentoF =='3':
            acumulador += 7
            continue # volta para o inicio do while True
        elif acompanhamentoF == '4':
            acumulador += 3
            continue # volta para o inicio do while True
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3/4!')
#Fim da função acompanhamentoFeijoada ()

#Início do Main
print('---------- Bem-vindo ao programa de feijoada do Patrik T. Saraiva ----------')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = (volume * opcao) + acompanhamento
print('O valor a ser pago é: R$ {:.2f} (Volume: R$ {:.2f}, Opção: R$ {:.2f}, Acompanhamento: R$ {:.2f})' .format(total,volume,opcao,acompanhamento))
