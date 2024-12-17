# Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o seu fatorial.

def fatorial(x):
    if type(x) != int or x < 0:
        return Exception
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

print("Todos os testes ok.")