def real_converter(moeda_a_converter, numero_reais):
    if(moeda_a_converter.lower() == "euro"):
        return numero_reais * 0.16
    elif(moeda_a_converter.lower() == "dolar"):
        return numero_reais * 0.17
    elif(moeda_a_converter == "pesos argentinos"):
        return numero_reais * 183.58
    elif(moeda_a_converter == "rupias indianas"):
        return numero_reais * 14.62

print("--Conversor de Reais--\n")

moeda_a_converter = (input("Insira a moeda para que você quer converter seus reais (pode ser: Dolar, Euro, Pesos Argentinos, Rupias Indianas):\n"))
numero_reais = float(input("Insira a quantidade de reais à converter:\n"))

print(f"O resultado final da conversão é: {real_converter(moeda_a_converter, numero_reais)} {moeda_a_converter + "s"}")

