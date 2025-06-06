palavra = input("Digite uma palavra:\n")

for letra in palavra:
    if(letra in "abc"): #se letra esta dentro de "abc" ("a" "b" "c")
        print("s")
    else:
        print("n")