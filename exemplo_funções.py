def resposta1():
    print("Boa escolha, acertou.")
def resposta2():
    print("*Você perdeu*")
def resposta3():
    print("Quase, tente de novo...")
def resposta_final():
    print("Você passou!")

while(True):
    escolha1 = input("2 + 2 = ?")
    if(escolha1 != "4"):
        resposta3()
    else:
        resposta1()
        break
while(True):
    escolha2 = input("6 * 3 = ?")
    if(escolha2 == "18"):
        resposta1()
        resposta_final()
        break
    else:
        resposta2()
        break
