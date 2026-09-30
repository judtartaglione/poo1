try:
    from src.personagem import Personagem
except ModuleNotFoundError:
    from personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=100,
            ataque=18,
            defesa=10
        )

    def atacar(self, alvo):
        dano = self.ataque
        alvo.receber_dano(dano)
        print(f"{self.nome} atirou uma flecha em {alvo.nome} e causou {dano} de dano.")
        return dano
