#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 08/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

def lista(n):
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
    for i in d:
        if d[i] > 1:
            return True
    return False

assert lista([2, 3, 4, 5, 6, 7]) == False    
assert lista([2, 2, 3, 3, 4, 4, 5]) == True
assert lista([2, 2, 1, 3]) == True
assert lista([1, 2, 3, 4, 5, 100, 101]) == False

assert lista([]) == Exception
assert lista(["3", 3, 4, 5]) == Exception
assert lista([True, 3, 4]) == Exception
assert lista([2.3, 2.3, 4, 5, 6]) == Exception
assert lista({2, 3, 4}) == Exception

print("Todos os testes ok.")