nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
if nome == 'Vinicius':
    print('Olá Vinicius!')
elif idade < 18:
    print('Você não é o Vinicius! E é menor de idade!')
elif idade > 100:
    print('Diferente de você, o Vinicius não é imortal!')
