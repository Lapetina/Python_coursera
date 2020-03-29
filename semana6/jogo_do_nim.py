"""
Jogo do NIM

Dois jogadores: Usuário e Computador

podem retirar 1 e no máximo M peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Estratégia par ganhar o jogo: deixar múltiplos de (m+1) peças ao jogador oponente.
Obs.: para ser múltiplo, é necessário que o resto da divisão seja 0

Computador sempre deve ganhar, para isso seguir a estratégia vencedora

Sejam n o número de peças inicial e M o número máximo de peças que é possível retirar em uma rodada

n - número de peças inicial
m - número máximo de peças que é possível retirar em uma rodada

Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para
o início do jogo:

- Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a
partida com a frase "Você começa"

- Caso contrário (Se não), o computador toma a iniciativa de começar o jogo, declarando
"Computador começa"

Uma vez iniciado o jogo, a estratégia do computador para ganhar o jogo consiste em:

    deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.

    Se não for possível, deverá tirar o número máximo de peças possíveis.
"""


def computador_escolhe_jogada(n, m):
    removendo_peca = 1
    while removendo_peca != m:
        if (n - removendo_peca) % (m + 1) == 0:
            return removendo_peca
        else:
            removendo_peca += 1

    return removendo_peca


def usuario_escolhe_jogada(n, m):
    i = 1
    jogada = int(input(u"Quantas peças você vai tirar? "))
    while i != 0:
        if jogada > m or jogada < 1:
            print(u"\nOops! Jogada inválida! Tente de novo.\n")
            jogada = int(input(u"Quantas peças você vai tirar? "))
        else:
            i = 0
    return jogada


def partida():
    n = int(input(u"Quantas peças? "))  # numero de peças em jogo
    m = int(input(u"Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print(u"\nVocê começa!\n")
        while n != 0:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if jogada_usuario == 1:
                print(u"\nVocê tirou uma peça\n")
                if n == 1:
                    print(u"Agora resta uma peça.\n")
                else:
                    print(u"Agora restam {} peças.\n".format(n))
            else:
                print(u"\nVocê tirou {} peças".format(jogada_usuario))
                if n == 1:
                    print(u"Agora resta uma peça.\n")
                else:
                    print(u"Agora restam {} peças.\n".format(n))

            jogada_cpu = computador_escolhe_jogada(n, m)
            n -= jogada_cpu
            if jogada_cpu == 1:
                print(u"Computador tirou uma peça\n")
                if n == 0:
                    break
            else:
                print(u"Computador tirou {} peças\n".format(n))
                if n == 0:
                    break
        print(u"Fim do jogo! O computador ganhou!")
    else:
        print("Computador começa!\n")
        while n != 0:
            jogada_cpu = computador_escolhe_jogada(n, m)
            n -= jogada_cpu
            if jogada_cpu == 1:
                print(u"Computador tirou uma peça\n")
                if n == 0:
                    break
            else:
                print(u"Computador tirou {} peças\n".format(n))
                if n == 0:
                    break
            print(u"Agora restam {} peças\n".format(n))
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if jogada_usuario == 1:
                print(u"\nVocê tirou uma peça.\n")
                if n == 1:
                    print(u"Agora resta uma peça.\n")
                else:
                    print(u"Agora restam {} peças.\n".format(n))
            else:
                print(u"\n Você tirou {} peças.\n".format(jogada_usuario))
                if n == 1:
                    print(u"Agora resta uma peça.\n")
                else:
                    print(u"Agora restam {} peças.\n".format(n))
        print(u"Fim do jogo! O computador ganhou!")


def campeonato():
    i = 1
    while i <= 3:
        print("\n**** Rodada {} ****\n".format(i))
        partida()
        i += 1
    print("Placar: Você 0 x 3 Consumidor")


print("Bem vindo ao jogo do NIM! Escolha: \n")
opcao = int(input("1 - para jogar uma partida isolada\n"
                  "2 - para jogar um campenato "))
if opcao == 1:
    print("Você escolheu uma partida!")
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()
