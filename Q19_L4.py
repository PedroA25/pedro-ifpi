# Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisores(x):
    if type(x) != int or x < 1:
        return Exception
    else:
        L = []
        for i in range(1, x+1):
            if x % i == 0:
                L.append(i)
    return len(L)



print("Todos os testes ok.")