
porg_j = float(input("Digite o Número de porcentagem do juros (mensalmente): %"))
mes_acum = float(input("Digite o tempo da Divida:\n"))
num_val = float(input("Digite o valor do emprestimo:\n"))
juros = (input("Digite o juros (Simples ou Composto):\n"))
cal_val = 0

if(porg_j >= 10):
    cal_val = (porg_j / 100) + 1
elif(porg_j <= 10):
    cal_val = (porg_j / 10) + 1

aum_men = (cal_val * num_val) - num_val
contador = 0
resultado = 0

if(juros == "simples" or "Simples"):
    resultado = (aum_men * mes_acum) + num_val
    print(f"O total da dívida atual é {resultado}")
elif(juros == "composto" or "Composto"):
    while contador < mes_acum:
        cal_val * num_val
        contador += 1
    print(f"O toltal da dívida atual é {num_val}")
else:
    print("Definições Invalidas")

