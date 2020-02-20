"""
Exercício 1
Escreva um programa que receba um número natural nn na entrada e imprima n! (fatorial) na saída.

Exemplo:

Digite o valor de n: 5
120
Dica: lembre-se que o fatorial de 0 vale 1!
"""
from math import factorial

def calculo_fatorial():
    n = int(input("Digite o valor de n: "))
    c = n
    fat = 1
    while c > 0:
        fat *= c
        c -= 1
    return fat

print(calculo_fatorial())
