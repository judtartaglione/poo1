class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        if hasattr(personagem, "curar"):
            personagem.curar(self.valor)
            print(f"{personagem.nome} usou {self.nome} e recuperou {self.valor} de vida.")
            return True
        return False


class PocaoDeVida(Item):

    def __init__(self, valor=30):
        super().__init__("Poção de Vida", valor)
