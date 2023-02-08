print('---------- Bem-vindo ao programa de limpeza do Patrik Teixeira Saraiva RU 3925726 ----------')

#Início da função metragem_limpeza()
def metragem_limpeza():
    print('*******************************************************')
    print('---------- Menu 1 de 3 - Metragem da Limpeza ----------')
    while True:
        try:
            metragemL = int(input('Digite a metragem desejada (m²): \n' + '>> '))
            if metragemL >= 30  and metragemL < 300:
                return 60 + 0.3 * metragemL
            elif metragemL >= 300 and  metragemL < 700:
                return 120 + 0.5 * metragemL
            else:
                print('Valores abaixo de 30m² e acima de 700m² não são aceitos!')
                continue # retorna para o inicio do laço (retorna para pergunta)
        except ValueError: # Caso o usuário digite valores double ou string e não inteiros
            print('Pare de digitar valores não inteiros!')
#Fim da função metragem_limpeza()

#Início da função tipo_limpeza()
def tipo_limpeza():
    print('***************************************************')
    print('---------- Menu 2 de 3 - Tipo de Limpeza ----------')
    while True:
        tipoL = input('Qual tipo de limpeza deseja?\n' +
                       'B - Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                       'C - Completa - Indicada para sujeiras antigas e/ou não rotineiras - Aumenta em 30% o valor da limpeza! \n' +
                       '>> ')
        tipoL = tipoL.upper()
        tipoL = tipoL.strip()
        if tipoL == 'B':
            return  1.00
        elif tipoL == 'C':
            return 1.30
        else:
            print('Pare de digitar opções diferentes de B/C!')
            continue # retorna para inicio do laço (retorna para pergunta)
#Fim da função tipo_limpeza()

#Início da função adicional_limpeza()
def adicional_limpeza():
    print('*******************************************************')
    print('---------- Menu 3 de 3 - Serviços Adicionais ----------')
    acumulador = 0
    while True:
        sAdicionais = input('Deseja mais algum serviço adicional: \n' +
                                '0 - Não desejo mais nada (encerrar) \n' +
                                '1 - Passar 10 peças de roupas - R$ 10,00 \n' +
                                '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                                '3 - Limpera de 1 Geladeira/Freezer - R$ 20,00 \n' +
                                '>> ')
        if sAdicionais == '0':
            return acumulador
        elif sAdicionais == '1':
            acumulador += 10
            continue # volta para o inicio do while True
        elif sAdicionais == '2':
            acumulador += 12
            continue # volta para o inicio do while True
        elif sAdicionais =='3':
            acumulador += 20
            continue # volta para o inicio do while True
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3!')
#Fim da função adicional_limpeza()

#Início do Main
metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicionais = adicional_limpeza()
total = (metragem * tipo) + adicionais
print('O valor a ser pago é: R$ {:.2f} (Valor da limpeza por m²: R$ {:.2f} * Tipo: {:.2f} + Serviços adicionais: R$ {:.2f})' .format(total,metragem,tipo,adicionais))