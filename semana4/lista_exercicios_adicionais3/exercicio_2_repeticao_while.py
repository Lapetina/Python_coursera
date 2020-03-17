"""
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido
possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim"; se não existir, imprima "não".
"""

def verification(n):
    anterior = n % 10
    n = n // 10;
    adj_iguais = False;
    pos = 0

    while n > 0 and not adj_iguais:
        atual = n % 10
        if atual == anterior:
            adj_iguais = True
        else:
            pos += 1
        anterior = atual
        n = n // 10
    if adj_iguais:
        print("sim")
    else:
        print("não")

number = int(input("Digite um número inteiro: "))

verification(number)
