from abc import ABC, abstractmethod


class Personagem(ABC):

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.max_vida = vida
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        dano = max(0, dano)
        self.vida = max(0, self.vida - dano)

    def curar(self, quantidade):
        quantidade = max(0, quantidade)
        self.vida = min(self.max_vida, self.vida + quantidade)

    def adicionar_item(self, item):
        self.inventario.append(item)

    @abstractmethod
    def atacar(self, alvo):
        pass

    def mostrar_status(self):
        print(
            f"{self.nome} | "
            f"Vida: {self.vida} | "
            f"Ataque: {self.ataque} | "
            f"Defesa: {self.defesa}"
        )
