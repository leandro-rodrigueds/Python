import random

def jogar():
    

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativa = 0
    pontos = 1000

    print("Qual o nivel de dificuldade ?")
    print("(1) Fácil (2) Médio (3)Difícil", end="\n\n")

    nivel = int(input("Defina o nível:"))

    if(nivel == 1):
        total_tentativa = 20
    elif(nivel == 2):
        total_tentativa = 10
    else:
        total_tentativa = 5

    for rodada in range(1,total_tentativa + 1):
        

        print("Tentativa {} de {}".format(rodada,total_tentativa))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1):
            print("Você digitou um número menor que 1")
        elif(chute > 100):
            print("Você digitou um número maior que 100")
            continue

        acertou = chute == numero_secreto
        numero_maior = chute > numero_secreto
        numero_menor = chute < numero_secreto
        
        
        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(numero_maior):
                print("Você errou! O seu chute foi maior do que o numero secreto ")
            elif(numero_menor):
                print("Você errou! O seu chute foi menor do que o numero secreto ")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
