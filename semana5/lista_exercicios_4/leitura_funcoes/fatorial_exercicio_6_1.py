"""
Exercicio 6.1 - O número de combinações possíveis de m elementos em grupos de n elementos (n <= m)
é dada pela fórmula de combinação m!/((m-n)!n!).
Escrever um programa que lê dois inteiros m e n e calcula a combinação de m,n a n.
"""

m = int(input("Digite um número: "))
n = int(input("Digite um número: "))
n_fatorial = 1
m_fatorial = 1
count = 1

# calculando o fatorial de m
while count < m:
    count += 1
    m_fatorial *= count

# calculando o fatorial de N
count = 1
while count < n:
    count += 1
    n_fatorial *= count

# calculando o fatorial de m-n
count = 1
result = m - n
mn_fatorial = 1
while count < result:
    count += 1
    mn_fatorial *= count

print("Comb(", m, ",", n, "): ", m_fatorial / (mn_fatorial * n_fatorial))
