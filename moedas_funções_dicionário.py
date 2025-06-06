lista_valores = {
    "dolar": [0.17],
    "euro": [0.16],
    "pesos argentinos": [182.42],
    "rupias indianas": [14.58]
}
moeda_a_converter = ""
numero_reais = 0
numero_moedas = 0
def converter_real_cal():
    conversao_final = numero_reais * (lista_valores[moeda_a_converter][0])
    print(f"R$ {numero_reais} para {moeda_a_converter} ficarão: {conversao_final:.2f}")
def converter_moedas_para_real_cal():
    conversao_final_para_real = numero_moedas / (lista_valores[moeda_a_converter][0])
    print(f"{numero_moedas} {moeda_a_converter} para reais ficarão: {conversao_final_para_real:.2f}")

print("---Conversor de Reais---\n\n")
adicionar_moeda = (input("Antes de fazer conversões, você gostaria de adicionar alguma moeda ao sistema? (Sim ou Não):\n"))

if(adicionar_moeda.lower() == "não"):
    print("Digite se você quer converter reais para uma outra moeda ou alguma moeda para reais:")
    seletor_converter = float(input("1 - Converter reais 2 - Converter uma moeda para reais\n"))
    if(seletor_converter == 1):
        moeda_a_converter = input(f"Digite o nome da moeda que você quer converter seus reais, opções: {lista_valores.keys()}):\n")
        numero_reais = float(input("Digite a quantidade de reais à converter:\n"))
        converter_real_cal()
    elif(seletor_converter == 2):
        moeda_a_converter = input(f"Digite o nome da moeda para que você quer converter para reais, opções: {lista_valores.keys()}):\n")
        numero_reais = float(input(f"Digite a quantidade de {numero_moedas} à converter para reais:\n"))
        converter_moedas_para_real_cal()
    else:
        print("Digito inválido")
elif(adicionar_moeda.lower() == "sim"):
    while(adicionar_moeda.lower() == "sim"):
        tipo_moeda_add = (input("Digite o nome da moeda à adicionar:\n"))
        calculo_moeda_add = float(input("Digite o número para o calculo da nova moeda:\n"))
        lista_valores[tipo_moeda_add] = [calculo_moeda_add]
        print(f"A moeda {tipo_moeda_add} foi adicionada ao sistema, com o valor de conversão para real de {calculo_moeda_add}")
        adicionar_moeda = (input("Você quer adicionar outra moeda ao sistema? (sim ou não):\n"))
    if(adicionar_moeda.lower() == "não"):
        print("Digite se você quer converter reais para uma outra moeda ou alguma moeda para reais:")
        seletor_converter = float(input("1 - Converter reais 2 - Converter uma moeda para reais\n"))
        if(seletor_converter == 1):
            moeda_a_converter = input(f"Digite o nome da moeda que você quer converter seus reais, opções: {lista_valores.keys()}):\n")
            numero_reais = float(input("Digite a quantidade de reais à converter:\n"))
            converter_real_cal()
        elif(seletor_converter == 2):
            moeda_a_converter = input(f"Digite o nome da moeda para que você quer converter para reais, opções: {lista_valores.keys()}):\n")
            numero_reais = float(input(f"Digite a quantidade de {moeda_a_converter} à converter para reais:\n"))
            converter_moedas_para_real_cal()
        else:
            print("Digito inválido")
    else:
        print("Digito inválido")
else:
    print("Digito inválido")