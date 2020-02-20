"""
Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos
dígitos deste número na saída

Exemplo:
Digite um número inteiro: 123
6
"""
def soma_digitos(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

n = int(input("Digite um número inteiro: "))
print(soma_digitos(n))