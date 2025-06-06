import random
val_apos = float(input("Digite o Valor à apostar:\n"))
tip_apos = input("Digite o tipo de jogo (Padrão, 50/50, Multi, Soma, Kamikaze):\n").lower()
num_sor1 = random.randint(1,10)
num_sor2 = random.randint(1,2)
num_sor3 = random.randint(1,15)
num_sor33 = random.randint(1,15)
num_sor4 = random.randint(1,10)
num_sor44 = random.randint(1,10)
num_sor5 = random.randint(1,100)
val_fin = 0

if(tip_apos == "padrão"):
    chute = float(input("Escolha um Número entre 1 à 10:\n"))
    if(chute > 10):
        print("Digito Invalido")
    elif(val_apos % 1 != 0):
        print("Digito Invalido")
    elif(chute == num_sor1):
        val_fin = val_apos * 1.2
        print(f"Você ganhou! Seu crédito é {val_fin}")
    elif(chute != num_sor1):
        val_fin = val_apos * 0.90
        print(f"Você perdeu! Seu crédito é {val_fin}")
elif(tip_apos == "50/50"):
    chute = float(input("Escolha um Número entre 1 ou 2:\n"))
    if(chute > 2):
        print("Digito Invalido")
    elif(val_apos % 1 != 0):
        print("Digito Invalido")
    elif(chute == num_sor2):
        val_fin = val_apos * 1.03
        print(f"Você ganhou! Seu crédito é {val_fin}")
    elif(chute != num_sor2):
        val_fin = val_apos * 0.97
        print(f"Você perdeu! Seu crédito é {val_fin}")
elif(tip_apos == "multi"):
    chute = float(input("Escolha um Número entre 1 à 15:\n"))
    chute2 = float(input("Escolha outro Número entre 1 à 15:\n"))
    if(chute > 15):
        print("Digito Invalido")
    elif(val_apos % 1 != 0):
        print("Digito Invalido")
    elif(chute == num_sor3 or chute2 == num_sor33):
        val_fin = val_apos * 1.15
        print(f"Você acertou um número! Seu crédito é {val_fin}")
    elif(chute == num_sor3 and chute2 == num_sor33):
        val_fin = val_apos * 1.32
        print(f"Você acertou DOIS números!! Seu crédito é {val_fin}")
    elif(chute != num_sor3 and chute != num_sor33):
        val_fin = val_apos * 0.92
        print(f"Você perde! Seu crédito é {val_fin}")
elif(tip_apos == "soma"):
    chute = float(input("Escolha um números entre 1 e 20 se a soma de dois aleatórios forem este número você ganha:\n"))
    if(chute > 20):
        print("Digito Invalido")
    elif(val_apos % 1 != 0):
        print("Digito Invalido")
    elif(chute == num_sor4 + num_sor44):
        val_fin = val_apos * 1.30
        print(f"Você ganhou! Seu crédito é {val_fin}")
    elif(chute != num_sor4 + num_sor44):
        val_fin = val_apos * 0.85
        print(f"Você perdeu! Seu crédito é {val_fin}")
elif(tip_apos == "kamikaze"):
    chute = float(input("Escolha um Número entre 1 à 100:\n"))
    if(chute > 100):
        print("Digito Invalido")
    elif(val_apos % 1 != 0):
        print("Digito Invalido")
    elif(chute == num_sor5):
        val_fin = val_apos * 5.5
        print(f"Você ganhou! Seu crédito é {val_fin}")
    elif(chute != num_sor5):
        val_fin = val_apos * 0.90
        print(f"Você perdeu! Seu crédito é {val_fin}")