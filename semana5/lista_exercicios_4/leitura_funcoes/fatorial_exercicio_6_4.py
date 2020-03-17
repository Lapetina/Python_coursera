"""
Exercício 6.4
Usando as funções dos exercícios 6.2 e 6.3, escreva um programa que lê um inteiro n, n >= 0 e
imprime os coeficientes da expansão de (x+y) elevado a n.

Lembre-se de utilizar o esqueleto de programa com funções em Python.
"""


def main():
    # leitura do n
    n = int(input("Digite n: "))

    cont = 0
    while cont <= n:
        print("Coeficiente de x^%d y^%d: %d" % (n - cont, cont, combinacao(n, cont)))
        cont += 1


def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1  # o mesmo que cont = cont + 1
        k_fat *= cont  # o mesmo que k_fat = k_fat * cont

    return k_fat


def combinacao(m, n):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''

    return fatorial(m) / (fatorial(n) * fatorial(m - n))
