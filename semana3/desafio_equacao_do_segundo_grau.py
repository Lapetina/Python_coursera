"""
Crie e um programa que calcula as raízes de uma equação de segundo grau.

método math é para calcular raíz quadrada
"""
import math

a = float(input("Informe o valor de A\n"))
b = float(input("Informe o valor de B\n"))
c = float(input("informe o valor de C\n"))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raíz é: {}".format(raiz1))
else:
    if delta < 0:
        print("Esta equação não possui raizes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raíz é: {}".format(raiz1))
        print("A segunda raíz é: {}".format(raiz2))
