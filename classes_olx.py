class Olx:
    def __init__(self, nome_produto, preco_produto, local_produto, manual_produto):
        self.nome = nome_produto
        self.preco = preco_produto
        self.local = local_produto
        self.manual = manual_produto
    def apresentar(self):
        print(f"Nome: {self.nome}")
    def aprsentar_tudo(self):
        print(f"Nome: {self.nome}")
        print(f"Nome: {self.produto}")
        print(f"Nome: {self.nome}")

produto1 = Olx("carro")
produto1.apresentar()
produto1.aprsentar_tudo()

