preco = float(input("Informe o valor da mercadoria: "))
porcentagem = float(input("Agora informe o per-centual de desconto: "))

print("O valor do desconto é R$", (preco * porcentagem / 100))
print ("O valor a ser pago é R$", preco - (preco * porcentagem / 100))