"""Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada."""


number = int(input("Digite um número: "))
verify_3 = number % 3
verify_5 = number % 5

if verify_3 == 0:
    print("FizzBuzz")
else:
    if verify_5 == 0:
        print("FizzBuzz")
    else:
        print("{}".format(number))
