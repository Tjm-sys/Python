
#numero1 = 0
#numero2 = 0
#numero3 = 0
#operacao = ""
#resultado = 0

numero1 = float(input("Digite o Primeiro Numero:\n"))
numero2 = float(input("Digite o Segundo Numero:\n"))
operacao = (input("Digite a Operação (+, -, /, *, <, >, op3):\n"))

if(operacao == "+"):        #sistema lógico de igualdade
    resultado = numero1 + numero2
    print("resultado é: " ,resultado, "")
elif(operacao == "-"):      #sistema lógico de igualdade
    resultado = numero1 - numero2
    print("resultado é: " ,resultado, "")
elif(operacao == "/"):      #sistema lógico de igualdade
    resultado = numero1 / numero2
    print("resultado é: " ,resultado, "")
elif(operacao == "*"):      #sistema lógico de igualdade
    resultado = numero1 * numero2
    print("resultado é: " ,resultado, "")
elif(operacao == "<"):      #sistema lógico de igualdade
    if(numero1 < numero2):          #sistema lógico de comparação
        print(f"{numero1} é menor que {numero2}")
    elif(numero2 < numero1):        #sistema lógico de comparação
        print(f"{numero2} é maior que {numero1}")
    else:                           #se não é nada disto só sobra:
        print(f"Os dois numeros são iguas")
elif(operacao == ">"):
    if(numero1 > numero2):
        print(f"{numero1} é menor que {numero2}")
    elif(numero2 > numero1):
        print(f"{numero2} é maior que {numero1}")
    else:
        print(f"Os dois numeros são iguas")
elif(operacao == "op3"):
    numero3 = float(input("Digite o Terceiro Numero:\n"))
    if  ((numero1 < numero2) and (numero2 < numero3) and (numero1 < numero3)):
        print(f"O Número {numero3} é o Maior, o Número {numero2} é o do Meio e o {numero1} é o Menor.")
    elif((numero1 > numero2) and (numero2 < numero3) and(numero1 < numero3)):
        print(f"O Número {numero3} é o Maior, o Número {numero1} é o do Meio e o {numero2} é o Menor.")
    elif((numero1 < numero2) and (numero2 > numero3) and (numero1 < numero3)):
        print(f"O Número {numero2} é o Maior, o Número {numero3} é o do Meio e o {numero1} é o Menor.")
    elif((numero1 < numero2) and (numero2 > numero3) and (numero1 > numero3)):
        print(f"O Número {numero2} é o Maior, o Número {numero1} é o do Meio e o {numero3} é o Menor.")
    elif((numero1 > numero2) and (numero2 > numero3) and (numero1 > numero3)):
        print(f"O Número {numero1} é o Maior, o Número {numero2} é o do Meio e o {numero3} é o Menor.")
    elif((numero1 < numero2) and (numero2 > numero3) and (numero1 > numero3)):
        print(f"O Número {numero1} é o Maior, o Número {numero3} é o do Meio e o {numero2} é o Menor.")
# termina aqui