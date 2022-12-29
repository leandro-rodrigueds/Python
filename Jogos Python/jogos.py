import forca
import adivinhacao

def jogo():
    print("*********************************")
    print("         Escolha um Jogo         ")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Opção de jogo:"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    jogo()
