lista_funcionarios = []

#---------- COMEÇO cadastrar_funcionario ----------
def cadastrar_funcionario(id):
    print('Bem-vindo ao Cadastrar Funcionarios')
    print('Codigo do Funcionário: {}'.format(id))
    nome = input('Digite o Nome do Funcionário: ')
    setor = input('Digite o Setor do Funcionário: ')
    salario = input('Digite o Salário do Funcionário: ')
    dicionario_funcionario = {'id' : id,
                           'nome' : nome,
                           'setor' : setor,
                           'salário' : salario}
    lista_funcionarios.append(dicionario_funcionario.copy())
    print('Cadastro de funcionário realizado com sucesso!')

# ---------- FIM cadastrar_funcionario ----------

#---------- COMEÇO consultar-funcionarios ----------
def consultar_funcionarios():
    while True:
        try:
            print('Bem-vindo ao Consultar Funcionários')
            op_consultar = int(input('Entre com a opção desejada:\n'
                                    '1 - Consultar Todos os Funcionários\n'
                                    '2 - Consultar por ID\n'
                                    '3 - Consultar por Setor\n'
                                    '4 - Retornar\n'
                                    '>> '))
            if op_consultar == 1:
                print('Bem vindo ao Consultar Todos')
                for funcionario in lista_funcionarios: #Selecionar cada dicionario da minha lista ( cada funcionario da lista_funcionarios)
                    for key, value in funcionario.items(): # Selecionar cada conjundo chave/valor do dicionario (ex: 'nome' : Renan)
                        print(' {} : {}' .format(key,value))
            elif op_consultar == 2:
                print('Bem vindo ao Consultar por ID')
                entrada = int(input('Digite o ID desejado: '))
                for funcionario in lista_funcionarios:
                    if(funcionario['id'] == entrada):
                        for key, value in funcionario.items():
                            print('{} : {}'.format(key, value))
            elif op_consultar == 3:
                print('Bem vindo ao Consultar por Setor')
                entrada = input('Digite o Setor desejado: ')
                for funcionario in lista_funcionarios:
                    if(funcionario['setor'] == entrada):
                        for key, value in funcionario.items():
                            print('{} : {}'.format(key, value))
            elif op_consultar == 4:
                break
            else:
                print('Pare de digitar números que não existem no menu')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')
# ---------- FIM consultar_funcionarios ----------

#---------- COMEÇO remover_funcionario ----------
def remover_funcionario():
    print('Bem-vindo ao Remover Funcionários')
    entrada = int(input('Digite o ID desejado: '))
    for funcionario in lista_funcionarios:
        if (funcionario['id'] == entrada):
            lista_funcionarios.remove(funcionario)
            print('Funcionário Removido com Sucesso!')
# ---------- FIM remover_funcionario ----------

#---------- COMEÇO MAIN ----------

print('Bem-vindo ao Programa Controle de Funcionários do Patrik Teixeira Saraiva')
registroFuncionario = 7400
while True:
    try:
        opcao = int (input('Digite a Opção Desejada:\n'
                            '1-Cadastrar Funcionário\n'
                            '2-Consultar Funcionário\n'
                            '3-Remover Funcionário\n'
                            '4-Sair'
                            '\n>> '))
        if opcao == 1:
            registroFuncionario =  registroFuncionario + 1
            cadastrar_funcionario(registroFuncionario)
        elif opcao == 2:
            consultar_funcionarios()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print('Programa Finalizado!')
            break
        else:
            print('Pare de digitar números que não existem no menu')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')
# ---------- FIM MAIN ----------