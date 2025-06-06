
#nota1 = 0
#nota2 = 0
#nota3 = 0
media = 0

nota1 = float(input("Digite a nota do primeitro Tri:"))
nota2 = float(input("Digite a nota do segundo Tri:\n"))
nota3 = float(input("Digite a nota do terceiro Tri:\n"))

media = ((nota1 + nota2 + nota3) / 3)
print(f"Sua media é:{media}")

if(media < 5):
    print("Rodou Direto")
elif(media > 7):
    print("Passou Direto") 
elif((media >= 5) and (media <= 7)):
    print("Pegou Recuperação")

#else:      Isso também funciona
#    print("Pegou Recuperação")