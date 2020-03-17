"""
Exercicio 6.3 - Usando a função do exercício 6.2, escreva uma função que recebe dois inteiros,
m e n, como parâmetros e retorna a combinação m!/((m-n)!n!).
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


def combinacao(m, n):
     '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''
     m_fatorial = fatorial(m)
     mn_fatorial = fatorial(m - n)
     n_fatorial = fatorial(n)

     return (m_fatorial/(mn_fatorial*n_fatorial))

print(combinacao(5,4))
