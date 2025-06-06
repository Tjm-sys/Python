soma_idade = 0
soma_altura = 0

grupo = [ #abro um dicionário
    {
        "nome": "Thales",
        "idade": 14,
        "altura": 1.86
    }, #, adiciono outro "usuario"
    {
        "nome": "Felipe",
        "idade": 24,
        "altura": 1.63
    },
    {
        "nome": "Gustavo",
        "idade": 14,
        "altura": 1.80
    },
    {
        "nome": "João",
        "idade": 14,
        "altura": 1.70
    }
]

for pessoa in grupo:  #para cada "pessoa" no grupo então vai se repetir 4 vezes neste caso
    soma_idade += (pessoa["idade"])
print(f"Média das idades são: {soma_idade / len(grupo)}")  #len é como se foçe comprimento, já que está em uma operação já é utilizado aquele número

for pessoa in grupo:
    soma_altura += (pessoa["altura"])
print(f"Média das alturas são: {soma_altura / len(grupo)}") #len é como se foçe comprimento, já que está em uma operação já é utilizado aquele número

for pessoa in grupo:
    print(f"Nomes: {pessoa["nome"]}")  #lista os "nome"s do dicionário grupo
