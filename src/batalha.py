class Batalha:

    def __init__(self, jogador, inimigo, pode_usar_itens=True):
        self.jogador = jogador
        self.inimigo = inimigo
        self.pode_usar_itens = pode_usar_itens

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")

            proxima_opcao = 2
            if hasattr(self.jogador, "usar_magia"):
                print(f"{proxima_opcao} - Usar magia")
                proxima_opcao += 1

            if self.pode_usar_itens:
                print(f"{proxima_opcao} - Usar item")
                proxima_opcao += 1

            print(f"{proxima_opcao} - Fugir")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)

            elif hasattr(self.jogador, "usar_magia") and opcao == "2":
                self.jogador.usar_magia(self.inimigo)

            elif self.pode_usar_itens and opcao == str(3 if hasattr(self.jogador, "usar_magia") else 2):
                if not self.jogador.inventario:
                    print("Você não possui itens no inventário.")
                    continue

                item = self.jogador.inventario.pop(0)
                item.usar(self.jogador)

            elif opcao == str(proxima_opcao):
                print("Você fugiu da batalha!")
                return

            else:
                print("Opção inválida.")
                continue

            if not self.inimigo.esta_vivo():
                break

            print("\n--- TURNO DO INIMIGO ---")
            self.inimigo.atacar(self.jogador)

        if not self.jogador.esta_vivo():
            print(f"{self.inimigo.nome} venceu a batalha!")
        elif not self.inimigo.esta_vivo():
            print(f"{self.jogador.nome} venceu a batalha!")
