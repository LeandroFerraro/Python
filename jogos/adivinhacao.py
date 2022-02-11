import random

def jogar_adivinhacao():
    print("*********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 100))
    total = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total = 3
    elif (nivel == 2):
        total = 2
    elif (nivel == 3):
        total = 1

    ##while (rodada <= total):
    for rodada in range(1,total+1):
        print("*********************************")
        print("Tentativa {} de {}".format(rodada, total))
        print("Você tem ", pontos)
        chute = int(input("Digite o seu número entre 1 e 100: "))

        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if (numero_secreto == chute):
            print("Você acertou e fez {} pontos!".format(pontos))
            rodada = 4
            break
        else:
            if(chute > numero_secreto):
                print("Você errou", end="\n")
                print("Seu chute foi maior que o numero secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            else:
                print("Você errou", end="\n")
                print("Seu chute foi menor que o numero secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        if (rodada == total):
            print("Você perdeu! :( \nO número secreto é {}".format(numero_secreto))

        rodada = rodada + 1
    print("Pontuação:", pontos)
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar_adivinhacao()