"""
Exercicio 6.2 - Complete a função fatorial abaixo, que recebe como parâmetro um número inteiro k,
k >= 0, e retorna k!.

Escreva apenas o corpo da função. Observe que o código já inclui chamadas para a função fatorial,
para que você possa testar a função.

def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1

    # COMPLETE ESSA FUNÇÃO

    return k_fat

# testes
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("17! =", fatorial(17))
"""
def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    count = 1
    while count < k:
        count += 1
        k_fat *= count

    total_fatorial = k_fat
    return total_fatorial


# testes
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("17! =", fatorial(17))