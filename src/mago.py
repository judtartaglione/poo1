try:
    from src.personagem import Personagem
except ModuleNotFoundError:
    from personagem import Personagem


class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5
        )

        self.mana = 100

    def atacar(self, alvo):
        dano = self.ataque
        alvo.receber_dano(dano)
        print(f"{self.nome} lançou um golpe simples em {alvo.nome} e causou {dano} de dano.")
        return dano

    def usar_magia(self, alvo):
        custo = 20

        if self.mana < custo:
            print("O mago não possui mana suficiente.")
            return 0

        self.mana -= custo
        dano = self.ataque + 20
        alvo.receber_dano(dano)
        print(f"{self.nome} usou magia em {alvo.nome} e causou {dano} de dano.")
        return dano
