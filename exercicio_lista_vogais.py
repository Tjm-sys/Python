palavra = input("Digite a palavra:\n")
numero_vogais = 0

for letra in palavra:
    if(letra.lower() in "aeiou"): # se letra (transforma em minusculo = lower() somente nesta equação) esta dentro de "aeiou"
        numero_vogais += 1
    else:
        numero_vogais += 0  #é inútil, mas é para completar o formato lógico da programação
print(f"o número de vogais da palavra {palavra} é: {numero_vogais}")