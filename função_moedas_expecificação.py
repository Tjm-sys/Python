def real_pra_rupia(real):
    return (real * 14.65) # "return = devolver, joga de volta algo"

print("---Conversor de Moedas---\n")
brl = float(input("Insira a moeda BRL e para qual moeda você quer converter:"))
inr = real_pra_rupia(brl) #define que "inr" = brl com a função aplicada
print(f"R${brl:.2f} = ₹{inr:.2f}") # o ".:2f" faz que o número termine em somente 2 casas depois da vírgula