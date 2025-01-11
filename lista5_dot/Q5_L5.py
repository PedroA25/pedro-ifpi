#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 11/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
# [1,3,6]

def cumulativa(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    l = []
    soma = 0
    for i in n:
        soma += i
        l.append(soma)
    return l

assert cumulativa([1, 4, 6]) == [1, 5, 11]
assert cumulativa([1, 2, 3]) == [1, 3, 6]
assert cumulativa([20, 30, 12]) == [20, 50, 62]
assert cumulativa([-2, -30, -11, 40, 22, 12]) == [-2, -32, -43, -3, 19, 31]
assert cumulativa([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 17, 24, 30, 35, 39, 42, 44, 45]

assert cumulativa([]) == Exception
assert cumulativa(["r", 2, 3, 4, 5, 6]) == Exception
assert cumulativa([True, Exception, 2, 3, 4, 5]) == Exception
assert cumulativa([2.3, 2.3, 4, 6.6, 4]) == Exception
assert cumulativa([None]) == Exception
assert cumulativa({2, 3, 4, 5, 6}) == Exception

print("Todos os testes ok.")
