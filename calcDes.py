valor_inicial = float(input("Digite o seu valor inicial da compra:\n"))
tipo_cliente = input("Digite o seu tipo de cliente(comum, vip, premium):\n").lower()
if(tipo_cliente == "comum"):
    print(f"{valor_inicial}")
elif(tipo_cliente == "vip"):
    valor_inicial = valor_inicial * 0.9
    print(f"{valor_inicial}")
elif(tipo_cliente == "premium"):
    valor_inicial = valor_inicial * 0.8
    print(f"{valor_inicial}")
else:
    print("Categoria Invalida")