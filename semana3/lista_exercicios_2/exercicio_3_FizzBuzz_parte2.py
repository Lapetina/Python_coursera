"""
Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
"""
number = int(input("Digite um número: "))
verify = number % 5

if verify == 0:
    print("Buzz")
else:
    print("{}".format(number))
