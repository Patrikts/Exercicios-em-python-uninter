print("Bem vindo a loja do Patrik Teixeira Saraiva") #Coloque o seu nome na Atividade Prática

valorProduto = float(input("Entre com o valor do produto: "))
qtdProduto = int (input("Entre com a quantidade: "))

subtotal = valorProduto * qtdProduto

if 0 <= qtdProduto < 11:
    valorFinal = subtotal + 30 # valor do frete = 30 R$
elif 11 <= qtdProduto < 101:
    valorFinal = subtotal + 60 # valor do frete = 60 R$
elif 101 <= qtdProduto < 1001:
    valorFinal = subtotal + 120 # valor do frete = 120 R$
else:
    valorFinal = subtotal + 240 # valor do frete = 240 R$

print("O valor sem o frete foi: R$ {:.2f}". format(subtotal)) # print do valor sem o frete
print("O valor com o frete foi: R$ {:.2f}". format(valorFinal)) # print do valor com o frete
print("O valor do frete foi: R$ {:.2f}". format(valorFinal - subtotal)) # print do valor do frete

