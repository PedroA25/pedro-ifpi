# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

import math

def equacao(x):
    if type(x) != int or x <= 0:
        return Exception
    return sum(1/ math.factorial(i) for i in range(x + 1))

print("Todos os testes ok.")