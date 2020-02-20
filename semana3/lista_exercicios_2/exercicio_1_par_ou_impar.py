"""Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.
"""
number = int(input("Digite o número: "))

verify = number % 2

if verify == 0:
    print("O número {} é par.".format(number))
else:
    print("O número {} é impar.".format(number))
