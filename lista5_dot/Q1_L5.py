#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 07/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

def repeticoes(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(n) != int:
            return Exception
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    return l

assert repeticoes([2, 2, 4, 5, 6, 6, 7]) == [2, 4, 5, 6, 7]
assert repeticoes([2,3,4,4,4,4,4,4]) == [2, 3, 4]
assert repeticoes([2, 2, 2, 2, 2]) == [2]

assert repeticoes(2) == Exception
assert repeticoes([-1, 3, -2, 5, 6, 7, 7]) == [-1, 3, -2, 5, 6, 7]
assert repeticoes([2.3, 2.3, 4, 4, 5]) == Exception
assert repeticoes(['b', 2, 3, 4, 4, 45]) == Exception

print("Todos os testes ok.")