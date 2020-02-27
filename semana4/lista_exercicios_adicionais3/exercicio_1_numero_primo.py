"""
Exercício 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplo:

Digite um número inteiro: 13
primo

Digite um número inteiro: 12
não primo
"""
def numbero_primo(numero):
    mult = 0
    for count in range(2,numero):
        if numero % count == 0:
            mult += 1
    if mult == 0:
       print("É primo")
    else:
        print("Não é primo")

numero = int(input("Digite um número inteiro:"))
numbero_primo(numero)