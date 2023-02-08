#---------COMEÇO DA FUNÇÃO SERVICOCAO---------
def servicoCao():
    while True:
        servicoC = input("Escolha o serviço desejado:\nBA - Banho\nTO - Tosa\nBT - Banho e Tosa\n>>")
        if servicoC == "BA":
            return 10.00
        elif servicoC == "TO":
            return 20.00
        elif servicoC == "BT":
            return 25.00
        else:
            print("Pare de digitar serviços que não existem. Tente de novo")
            continue
#---------FIM DA FUNÇÃO SERVICOCAO---------
#---------COMEÇO DA FUNÇÃO PESOCAO---------
def pesoCao():
    while True:
        try:
            pesoC = float (input("Entre com o peso do cachorro (kg): "))
            if 0 <= pesoC <= 10:
                return 1.5
            elif (pesoC > 10) and (pesoC <= 20):
                return 2.0
            elif 20 < pesoC <= 30:
                return 2.5
            elif 30 < pesoC <= 40:
                return 3.0
            elif pesoC > 40:
                return 4.0
            else:
                print("Não aceitamos cachorros com peso negativo")
                continue
        except ValueError:
            print("Pare de digitar valores não numéricos. Tente novamente")
            continue
#---------FIM DA FUNÇÃO PESOCAO---------
#---------COMEÇO DA FUNÇÃO PELOCAO---------
def peloCao():
    while True:
        peloC = input("Entre com o pelo do cachorro:\nC - Curto\nM - Médio\nL - Longo\n>>")
        if peloC == "C":
            return 1.5
        elif peloC == "M":
            return 2.0
        elif peloC == "L":
            return 2.5
        else:
            print("Pare de digitar pelos que não existem. Tente de novo")
            continue
#---------FIM DA FUNÇÃO PELOCAO---------
#------------COMEÇO DA MAIN-------------
print("Bem vindo ao PetShop do Patrik T. Saraiva")
#servico = servicoCao()
#peso = pesoCao()
#pelo = peloCao()
#total = servico * peso * pelo
print("O valor total foi de: R$ {:.2f}" .format(servicoCao() * pesoCao() * peloCao()))

#---------FIM DA MAIN---------
