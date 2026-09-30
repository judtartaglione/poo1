try:
    from src.arqueiro import Arqueiro
    from src.batalha import Batalha
    from src.guerreiro import Guerreiro
    from src.inimigo import Assassino, ChefeFinal, Inimigo
    from src.item import PocaoDeVida
    from src.mago import Mago
except ImportError:
    from arqueiro import Arqueiro
    from batalha import Batalha
    from guerreiro import Guerreiro
    from inimigo import Assassino, ChefeFinal, Inimigo
    from item import PocaoDeVida
    from mago import Mago


def criar_jogador(opcao, nome):
    if opcao == "1":
        return Guerreiro(nome)
    if opcao == "2":
        return Mago(nome)
    if opcao == "3":
        return Arqueiro(nome)
    raise ValueError("Classe inválida")


def criar_inimigo(opcao, nome):
    if opcao == "1":
        return Inimigo(nome, 60, 15, 5)
    if opcao == "2":
        return Assassino(nome, 35, 18, 8)
    if opcao == "3":
        return ChefeFinal(nome)
    raise ValueError("Tipo de inimigo inválido")


def escolher_classe():
    print("Escolha a classe do seu personagem:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")

    opcao = input("Digite a opção desejada: ")
    nome = input("Digite o nome do personagem: ")

    try:
        jogador = criar_jogador(opcao, nome)
    except ValueError:
        print("Opção inválida. Escolha novamente.")
        return escolher_classe()

    return jogador


def escolher_inimigo():
    print("Escolha o tipo de inimigo:")
    print("1 - Inimigo comum")
    print("2 - Assassino")
    print("3 - Chefe final")

    opcao = input("Digite a opção desejada: ")
    nome = input("Digite o nome do inimigo: ")

    try:
        return criar_inimigo(opcao, nome)
    except ValueError:
        print("Opção inválida. Escolha novamente.")
        return escolher_inimigo()


def escolher_uso_itens():
    resposta = input("Deseja usar itens durante a batalha? (s/n): ").strip().lower()
    return resposta in {"s", "sim", "y", "yes"}


def main():
    jogador = escolher_classe()
    jogador.adicionar_item(PocaoDeVida())

    inimigo = escolher_inimigo()
    pode_usar_itens = escolher_uso_itens()

    batalha = Batalha(jogador, inimigo, pode_usar_itens=pode_usar_itens)
    batalha.iniciar()


if __name__ == "__main__":
    main()
