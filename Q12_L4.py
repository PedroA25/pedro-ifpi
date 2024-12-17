# Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.

def ordenados(a, b):
    if type(a) != int or type(b) != int:
        return Exception
    if a > b:
        return (b, a)
    elif b > a:
        return (a, b)

assert ordenados(3, 1) == (1, 3)

print("Todos os testes ok.")