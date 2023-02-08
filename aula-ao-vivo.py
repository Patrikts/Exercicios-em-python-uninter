print("Bem vindo a loja do Patrik Teixeira Saraiva") #Coloque o seu nome na Atividade Prática
valorProduto = float(input("Entre com o valor do produto: "))
qtdProduto = int (input("Entre com a quantidade: "))
subtotal = valorProduto * qtdProduto
if 0 <= subtotal < 200:
    valorFinal = subtotal
elif 200 <= subtotal < 400: # subtotal >= 200 and subtotal <= 400
    valorFinal = subtotal - subtotal * 0.04 # desconto de 4%
elif 400 <= subtotal < 700:
    valorFinal = subtotal - subtotal * 0.07 # desconto de 7%
else: # se o valor for acima de 700 entra nesse else
    valorFinal = subtotal - subtotal * 0.10 # desconto de 10 %
print(valorFinal)

print("O valor sem desconto: R$ {:.2f}". format(subtotal))
print("O valor com desconto: R$ {:.2f}". format(valorFinal))