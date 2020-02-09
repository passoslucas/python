
def main():
    import random
    import jogos
    jogar_denovo = 1
    while jogar_denovo == 1:
        print("*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")

        numero_sereto = round(random.randrange(1, 11))
        pontos = 100
        tentativas = 1

        print("Qual o nível de dificuldade?")
        print("[1] Fácil [2] Médio [3] Difícil")
        nivel = int(input("Defina o Nível: "))

        for cont in range(4):
            if nivel == 1:
                tentativas = 6
                break
            elif nivel == 2:
                tentativas = 4
                break
            elif nivel == 3:
                tentativas = 2
                break
            else:
                print("Valor Inválido!")
                nivel = int(input("Defina o Nível: "))

        for x in range(1, tentativas + 1):
            print("Tentativa {} de {}".format(x, tentativas))
            chute = int(input("Digite o seu número de 1 a 10: "))

            if chute < 1 or chute > 10:
                print("Número inválido! Você deve digitar um número de 1 a 10!")
                continue

            acertou = numero_sereto == chute
            maior = numero_sereto < chute

            print("Você digitou ", chute)

            if acertou:

                print("Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if maior:
                    print("Você errou! Mais baixo...")
                else:
                    print("Você errou! Mais alto...")
                pontos_perdidos = abs(numero_sereto - chute) * 3
                pontos = pontos - pontos_perdidos

        print("Fim do Jogo")

        jogar_denovo = int(input("Jogar novamente? (1) SIM (2) NÃO: "))

        if jogar_denovo == 1:
            jogar_denovo = 1
            print("Novo jogo...")

        else:
            print("Menu...")
            jogos.menu()


if __name__ == "__main__":
    main()

else:
    main()
