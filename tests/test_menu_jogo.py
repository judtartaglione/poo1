from src.arqueiro import Arqueiro
from src.guerreiro import Guerreiro
from src.inimigo import Assassino, ChefeFinal, Inimigo
from src.main import criar_inimigo, criar_jogador
from src.mago import Mago


def test_criar_jogador_por_classe():
    assert isinstance(criar_jogador("1", "Arthur"), Guerreiro)
    assert isinstance(criar_jogador("2", "Merlin"), Mago)
    assert isinstance(criar_jogador("3", "Lia"), Arqueiro)


def test_criar_inimigo_por_tipo():
    assert isinstance(criar_inimigo("1", "Goblin"), Inimigo)
    assert isinstance(criar_inimigo("2", "Ladrão"), Assassino)
    assert isinstance(criar_inimigo("3", "Rei das Sombras"), ChefeFinal)
