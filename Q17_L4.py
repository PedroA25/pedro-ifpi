# Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.

from random import randint

def maior_menor(x):
    if len(x) != 50:
        return Exception
    return (max(x), min(x))

assert maior_menor([num for num in range(1, 51)]) == (50, 1)

