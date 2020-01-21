'''
Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e
imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:

Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
'''

def calculo_quadrado(x):
    area = x ** 2
    perimetro = x * 4

    return area, perimetro

lado = int(input("Digite o valor correspondente ao lado de um quadrado: \n"))
area, perimetro = calculo_quadrado(lado)
print("perímetro: {} - área: {} ".format(perimetro, area))
