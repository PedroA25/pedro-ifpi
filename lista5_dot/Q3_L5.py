#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 11/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25

def maior_soma(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    
    maior = n[0] + n[1]

    for i in range(len(n) - 1):
        soma = n[i] + n[i+1]
        if soma > maior:
            maior = soma
    return maior

assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1])
assert maior_soma([19, 2, 3, 4, 6, 28, 5]) == 34
assert maior_soma([-11, 3, -45, 2, 64, -3, 2, 12, -10, 4]) == 66
assert maior_soma([23, 4, 5, -1, -4, 5, 8, 10, 3]) == 27
assert maior_soma([-6, -4, -34, -21, -31, -2, -6, -5]) == -8

assert maior_soma([]) == Exception
assert maior_soma(["w", 2, 3, 4, 5, 6, 8, 10]) == Exception
assert maior_soma([True, False, 2, 1, 4, 5, 6]) == Exception
assert maior_soma([2.3, 2.3, 5.6, 4, 6, 8, 9, 10]) == Exception
assert maior_soma([{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}]) == Exception

print("Todos os testes ok.")
