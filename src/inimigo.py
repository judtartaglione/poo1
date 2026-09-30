try:
    from src.personagem import Personagem
except ModuleNotFoundError:
    from personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
        dano = self.ataque
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano.")
        return dano


class Assassino(Inimigo):

    def __init__(self, nome="Assassino", vida=25, ataque=12, defesa=6):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        dano = self.ataque + 4
        alvo.receber_dano(dano)
        print(f"{self.nome} executou um golpe furtivo em {alvo.nome} e causou {dano} de dano.")
        return dano


class ChefeFinal(Inimigo):

    def __init__(self, nome="Rei das Sombras", vida=200, ataque=30, defesa=20):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        dano = self.ataque + 10
        alvo.receber_dano(dano)
        print(f"{self.nome} usou golpe final em {alvo.nome} e causou {dano} de dano.")
        return dano
