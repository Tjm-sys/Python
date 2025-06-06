user_response = ""

while(user_response != "3"): #diferente de sair
    print("Bem-vindo a Padaria do Jorge")
    print()
    print("1) Fazer um pedido")
    print("2) Trabalhe conosco")
    print("3) Sair")
    user_response = input().lower()

    if(user_response == "1"):        
        print("")
        print("Você recebeu um pão") #retorna ao inicio
        print("")
    elif(user_response == "2"): #retorna ao inicio
        print("")
        print("eles não o aceitaram")
        print("")
    elif(user_response == "3"): #não irá repetir
        print("")
        print("até logo...")
        print("")
    print("boa resposta")