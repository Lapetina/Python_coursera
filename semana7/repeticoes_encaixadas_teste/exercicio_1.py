"""Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros
correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir
uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
##########
##########

digite a largura: 2
digite a altura: 2
##
##

Dica: lembre-se que a função print pode receber um parametro 'end', que altera o último
caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas) """

largura = int(input("digete a largura: "))
altura = int(input("digite a altura: "))

x = 0
while x < altura:
    x += 1
    y = 0
    while y < largura:
        print("#", end="")
        y += 1
    print("")
