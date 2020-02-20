"""
Exercício 2
Receba um número inteiro positivo na entrada e imprima os N primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9
"""

def calculo_n_impares(n):
    contador = 0
    numero_natural = 0
    while contador < n:
        resultado = numero_natural % 2
        if resultado == 0:
            numero_natural += 1
        else:
            print(numero_natural)
            numero_natural += 1
            contador += 1

numero = int(input("Digite o valor de n: "))

calculo_n_impares(numero)