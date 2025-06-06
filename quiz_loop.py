#quiz que diminui as tentativas a cada erro ou acerto se errar repete a pergunta
resposta = ""
tentativas = 10

while(resposta != "25"):
    print(f"Você tem {tentativas} tentativas")
    print("5 * 5 = ?")
    tentativas = tentativas - 1 #dinimui as tentativas, se for errada a resposta trava na pergunta até acertar
    resposta = str(input())
    if(resposta == 25):
        break
print("Resposta Certa!")

while(resposta != 48):
    print(f"Você tem {tentativas} tentativas")
    print("5 * 7 + 13 = ?")
    tentativas = tentativas - 1
    resposta = int(input())
    if(resposta == 48):
        break
print("Resposta Certa!")