#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

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
        L.append((num, N, N*num))
    return L

assert tabuada(2) == [(1, 2, 2), (2, 2, 4)]
assert tabuada(3) == [(1, 3, 3,), (2, 3, 6), (3, 3, 9)]
assert tabuada(4) == [(1, 4, 4), (2, 4, 8), (3, 4, 12), (4, 4, 16)]

assert tabuada(-3) == Exception
assert tabuada(True) == Exception
assert tabuada("w") == Exception
assert tabuada(2.4) == Exception

print("Todos os testes ok.")