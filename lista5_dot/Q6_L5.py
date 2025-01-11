#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 11/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

def true_false(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    if sorted(n) == n:
        return True
    else:
        return False

assert true_false([4, 5, 6, 7, 8, 9, 10]) == True
assert true_false([2, 3, 4, 5, 1, 0, -11]) == False
assert true_false([100, 102, 102, 103, 99]) == False
assert true_false([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True

assert true_false([]) == Exception
assert true_false(["n", 2, 3, 4, 5, 6]) == Exception
assert true_false([2.3, 22, 3, 4, 5]) == Exception
assert true_false([True, 2, 3, 4, 5, 6]) == Exception
assert true_false([None]) == Exception

print("Todos os testes ok.")