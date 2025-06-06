
import time
energia = 50
item = ""

print("*Você está sentado na cadeira do seu escritório do centro policial*")
time.sleep(1.5)
print("Um homem entra pela porta da frente da sala...")
time.sleep(1.5)
print("- Boa tarde senhor, tenho um problema, poderia me ajudar")
time.sleep(1.5)
choice1 = input(f"1 - Claro 2 - Não desculpe, estou com muito trabalho\n")

while(choice1 == "2"):
    print("- É muito importante")
    time.sleep(1.5)
    print("- Você não vai se arrepender")
    time.sleep(1.5)
    choice1 = input(f"1 - Ok, pode falar 2 - Eu realmente não posso senhor\n")
if(choice1 == "1"):
    print("- Eu estava em minha loja, no final do turno...")
    time.sleep(1.5)
    print("- Depois de ouvir um barulho, vi um dos meus funcionários deitado no chão com ferimentos graves.")
    time.sleep(1.5)
    print("- Chamei uma ambulância, mas ele não resistiu a caminho do hospital")
    time.sleep(1.5)
    choice2 = input("1 - Que pena 2 - Tinha mais alguém no local?\n")

while(choice2 == "1" ):
    print("Pois é")
    time.sleep(1.5)
    print("Tem mais alguma pergunta?")
    time.sleep(1.5)
    choice2 = input("1 - Não... 2 - Tinha mais alguém no local?\n")
if(choice2 == "2"):
    print("- Meu último funcionário tinha saido há 15 min")
    time.sleep(1.5)
    print("Ele não se dava muito bem com o colega fazia um tempo")
    time.sleep(1.5)
    choice3 = input("1 - Ir até a loja para investigar (-10 de energia) 2 - Procurar destemnunhas (-10 de energia)\n")

while(choice3 == "2"):
    energia -= 10
    print(f"Não achei ninguém disponivel no horário... (Sua energia é {energia})")
    time.sleep(1.5)
    print("Melhor tentar achar outra pista")
    time.sleep(1.5)
    choice3 = input("1 - Ir até a loja para investigar (-10 de energia) 2 - Procurar temnunhas (-10 de energia)\n")
if(choice3 == "1"):
    energia -= 10
    print(f"*Você acabou de chegar na loja* (Sua energia é {energia})")
    time.sleep(1.5)
    print("Logo de cara você vê três pistas...")
    time.sleep(1.5)
    choice4 = input("1 - Marcas de sangue 2 - Objeto afiado 3 - papel na mesa principal\n")
    time.sleep(1.5)

while(choice4 == "1"):
    energia -= 10
    print(f"Somente resquicios do crime... (Sua energia é {energia})")
    time.sleep(1.5)
    print("Nada além do conhecido.")
    time.sleep(1.5)
    choice4 = input("1 - Marcas de sangue 2 - Objeto afiado 3 - papel na mesa principal\n")
while(choice4 == "2"):
    energia -= 10
    print(f"Somente resquicios do crime... (Sua energia é {energia})")
    time.sleep(1.5)
    print("Nada além do conhecido.")
    time.sleep(1.5)
    choice4 = input("1 - Marcas de sangue 2 - Objeto afiado 3 - papel na mesa principal\n")
if(choice4 == "3"):
    energia -= 10
    print(f"Este é um documento em nome da loja (sua energia é {energia})")
    time.sleep(1.5)
    print("Diz sobre um adiamento de dividas...")
    time.sleep(1.5)
    print("Por evento anormal. Ótima pista, talvez o dono da loja esteja envolvido com o assassinato")
    time.sleep(1.5)
    choice5 = input("1 - Acusar o dono da loja 2 - Continuar investigando\n")

if(choice5 == "1"):
    if(energia <= 0):
        print("O jogo acabou, você tem que descansar.")
        exit()
    print("*Você chegou no seu escritório*")
    time.sleep(1.5)
    print("O homem estava te esperando...")
    time.sleep(1.5)
    print("Você o acusa do crime")
    time.sleep(1.5)
    print("Ele entra em pânico e tenta fugir rápidamente é pego por um colega seu")
    time.sleep(1.5)
    print("Ele é julgado e condenado a prisão")
    time.sleep(1.5)
    print("O caso acabou... FIM")
elif(choice5 == "2"):
    if(energia <= 0):
        print("O jogo acabou, você tem que descansar.")
        exit()
    print("*Você continua investigando a loja*")
    time.sleep(1.5)
    print("Não consegue achar nada")
    time.sleep(1.5)
    print("O caso é arquivado e suspenso")
    time.sleep(1.5)
    print("A loja continua com a divida suspensa, e o criminoso a solta")
    time.sleep(1.5)
    print("O caso continua... Fim")
