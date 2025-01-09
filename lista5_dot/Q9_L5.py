#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 08/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
# [7, 3]

def repeticoes(n):
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
        if d[i] == 1:
            l.append(i)
    return l

assert repeticoes([3, 4, 4, 5, 6]) == [3, 5, 6]
assert repeticoes([3, 3, 6, 6, 8, 8, 9]) == [9]
assert repeticoes([1, 1, 2]) == [2]
assert repeticoes([1, 1]) == []

assert repeticoes([]) == Exception
assert repeticoes(["e", 2, 2, 3, 4, 5, 5, 8]) == Exception
assert repeticoes([True, 2, 3, 4, 4, 5, 5]) == Exception
assert repeticoes([2.3, 2.3, 4, 5, 5]) == Exception

print("Todos os testes ok.")
