listaEstudantes = []

#---------- COMEÇO cadastrarEstudante ----------
def cadastrarEstudante(ru):
    print('Bem-vindo ao Cadastrar Estudantes')
    print('O RU do estudante a ser cadastrado é: {}'.format(ru))
    nome = input('Digite o nome do estudante: ')
    turma = input('Digite a turma do estudante: ')
    dicionarioEstudante = {'ru' : ru,
                           'nome' : nome,
                           'turma' : turma}
    listaEstudantes.append(dicionarioEstudante.copy())
    print('Cadastro de estudante realizado com sucesso!')

# ---------- FIM cadastrarEstudante ----------

#---------- COMEÇO consultarEstudante ----------
def consultarEstudante():
    while True:
        try:
            print('Bem-vindo ao Consultar Estudantes')
            opConsultar = int(input('Entre com a opção desejada:\n'
                                    '1 - Consultar Todos os Estudantes\n'
                                    '2 - Consultar por RU\n'
                                    '3 - Consultar por Turma\n'
                                    '4 - Retornar\n'
                                    '>> '))
            if opConsultar == 1:
                print('Bem vindo ao Consultar Todos')
                for estudante in listaEstudantes: #Selecionar cada dicionario da minha lista ( cada estudante da listaEstudantes
                    for key, value in estudante.items(): # Selecionar cada conjundo chave/valor do dicionario (ex: 'nome' : Renan)
                        print(' {} : {}' .format(key,value))
            elif opConsultar == 2:
                print('Bem vindo ao Consultar por RU')
                entrada = int(input('Digite o RU desejado: '))
                for estudante in listaEstudantes:
                    if(estudante['ru'] == entrada):
                        for key, value in estudante.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                print('Bem vindo ao Consultar por Turma')
                entrada = input('Digite a turma desejada: ')
                for estudante in listaEstudantes:
                    if(estudante['turma'] == entrada):
                        for key, value in estudante.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                break
            else:
                print('Pare de digitar números que não existem no menu')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')
# ---------- FIM consultarEstudante ----------

#---------- COMEÇO removerEstudante ----------
def removerEstudante():
    print('Bem-vindo ao Remover estudantes')
    entrada = int(input('Digite o RU desejado: '))
    for estudante in listaEstudantes:
        if (estudante['ru'] == entrada):
            listaEstudantes.remove(estudante)
            print('Estudante Removido com Sucesso!')
# ---------- FIM removerEstudante ----------

#---------- COMEÇO MAIN ----------

print('Bem-vindo ao Programa Controle de Estudantes Patrik Teixeira Saraiva')
registroAcademico = 0
while True:
    try:
        opcao = int (input('Digite a Opção Desejada:\n'
                            '1-Cadastrar Estudante\n'
                            '2-Consultar Estudante\n'
                            '3-Remover Estudante\n'
                            '4-Sair'
                            '\n>> '))
        if opcao == 1:
            registroAcademico =  registroAcademico + 1
            cadastrarEstudante(registroAcademico)
        elif opcao == 2:
            consultarEstudante()
        elif opcao == 3:
            removerEstudante()
        elif opcao == 4:
            print('Programa Finalizado!')
            break
        else:
            print('Pare de digitar números que não existem no menu')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')
# ---------- FIM MAIN ----------
