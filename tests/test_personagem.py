from src.guerreiro import Guerreiro
from src.inimigo import Inimigo


def test_guerreiro_esta_vivo():
    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    guerreiro = Guerreiro("Arthur")

    guerreiro.receber_dano(20)

    assert guerreiro.vida == 100


def test_personagem_morre():
    guerreiro = Guerreiro("Arthur")

    guerreiro.receber_dano(200)

    assert guerreiro.vida == 0
    assert guerreiro.esta_vivo() is False


def test_personagem_cura_nao_excede_maximo():
    guerreiro = Guerreiro("Arthur")
    guerreiro.receber_dano(50)
    guerreiro.curar(200)

    assert guerreiro.vida == guerreiro.max_vida


def test_guerreiro_ataca():
    guerreiro = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 30, 10, 5)

    dano = guerreiro.atacar(inimigo)

    assert dano == 20
    assert inimigo.vida == 10
