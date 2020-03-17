"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e
devolve o maior número primo menor ou igual ao número passado à função.

Exemplo:
> maior_primo(100)
97
> maior_primo(7)
7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando
 se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado
 na variável é o maior primo encontrado.
 """


def maior_primo(number):
    primos = []
    for i in range(number):
        c = 0
        for j in range(number):
            if i % (j+1) == 0:
                c += 1
        if c == 2:
            primos.append(i)

    return max(primos)

