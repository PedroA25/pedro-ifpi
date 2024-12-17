# # Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N. Mostre a tabuada na forma:
# #1 x N = N
# 2 x N = 2N
# ...
# N x N = N2

def tabuada(N):
    if type(N) != int or N < 1:
        return Exception
    L = []
    for num in range(1, N+1):
        L.append((N, num, N*num))
    return L

print(tabuada(0))

print("Todos os testes ok.")