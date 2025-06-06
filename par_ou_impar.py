
numero1 = float(input("Digite o número:\n"))

if(numero1 % 1 != 0):
    print("O Número é Invalido")
else:
    if(numero1 % 2 == 0):
        print("É par")
    elif(numero1 % 2 != 0):
        print("É impar")