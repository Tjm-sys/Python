class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("thales", 14)
pessoa1.apresentar()

pessoa2 = Pessoa("josé", 0)
pessoa2.apresentar()
