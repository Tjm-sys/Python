convidados = []
nome = "a"

while(nome != ""):
    nome = input("Insira um nome para a lista de convidados:\n")
    convidados.append(nome)  #adiciona item (append(nome)) a lista no caso convidados
print("\n\n")
print("Lista de Convidados:")
for convidados in convidados:
    print(convidados)