"""
Exercício 2

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não
estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##
"""

largura = int(input("digete a largura: "))
altura = int(input("digite a altura: "))

linha = 1
while linha <= altura:
    print("#", end="")
    coluna = 2
    while coluna <= largura:
        # Se for a primeira linha, a última linha ou a última coluna
        if (linha == 1) or (linha == altura) or (coluna == largura):
            print("#", end="")
            coluna += 1
        else:
            print(end=" ")
            coluna += 1
    print("")
    linha += 1
