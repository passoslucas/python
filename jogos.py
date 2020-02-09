import forca
import adivinhacao


def menu():
    print("*********************************")
    print("****Qual jogo você quer jogar?***")
    print("*********************************")

    jogo = int(input("(1) Forca (2) Adivinhação: "))

    if jogo == 1:
        print("Inciando Forca...")
        forca.play_forca()
    elif jogo == 2:
        print("Iniciando Adivinhação...")
        adivinhacao.main()


if __name__ == "__main__":
    menu()

else:
    menu()
