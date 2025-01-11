#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 11/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
# 10, 3, 1] = 20

def maior_soma(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    d = {}
    for i in n:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    l = []
    for i in d:
        if d[i] > 1 :
            l.append(i)
    l1 = []
    for i in l:
        l1.append(i+i)
    return max(l1)

assert maior_soma([2, 2, 3, 4, 4, 5, 6, 6, 7]) == 12
assert maior_soma([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert maior_soma([9, 3, 4, 7, 7, 1, 1, 9, 8]) == 18
assert maior_soma([30, 30, 2, 1, 50, 23, 45, 45, 6]) == 90
assert maior_soma([-2, -4, -3, -1, -1, -2, -6, 7, 8]) == -2

assert maior_soma([]) == Exception
assert maior_soma(['t', 1, 2, 2, 5, 5, 9]) == Exception
assert maior_soma([True, False, 2, 3, 4, 4]) == Exception
assert maior_soma([2.3, 2.3, 2, 6, 6, 9]) == Exception
assert maior_soma({2, 2, 3, 3, 5, 6, 7, 7, 11}) == Exception

print("Todos os testes ok.")
