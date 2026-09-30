from src.batalha import Batalha
from src.guerreiro import Guerreiro
from src.inimigo import Assassino, ChefeFinal


def test_batalha_jogador_vence(monkeypatch):
    jogador = Guerreiro("Arthur")
    inimigo = Assassino("Ladrão", 15, 8, 4)
    batalha = Batalha(jogador, inimigo)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    batalha.iniciar()

    assert not inimigo.esta_vivo()
    assert jogador.esta_vivo()


def test_chefe_final_tem_vida_e_ataque_maiores():
    chefe = ChefeFinal("Rei das Sombras")
    jogador = Guerreiro("Arthur")

    chefao = chefe.atacar(jogador)

    assert chefe.vida > 100
    assert chefao >= 20
    assert jogador.vida < 120
