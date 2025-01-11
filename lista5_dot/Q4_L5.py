#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 11/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 34

def maior_soma(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    soma = n[0]
    maior = n[0]
    
    for i in range(1, len(n)):
        soma = max(n[i], soma + n[i])   
        maior = max(maior, soma)  
    
    return maior

assert maior_soma([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1])
assert maior_soma([1, -2, 3, 5, -1, 2, -1, -2]) == 9
assert maior_soma([-5, -1, -8, -9]) == -1
assert maior_soma([2, 4, 6, 8]) == 20
assert maior_soma([10, -3, 2, 1, -10, 5, 20, -1, -2, 8, -5, 3]) == 30

assert maior_soma([]) == Exception
assert maior_soma(["w", -2, 2, 3, 4, 5, 6, -5]) == Exception
assert maior_soma([True, False, 2, 3, 4, 5, 6]) == Exception
assert maior_soma([2.3, 2.3, 5, 7, 8, 9]) == Exception
assert maior_soma({2, 3, 4, 5, 6, 7, 8, 9, 10}) == Exception

print("Todos os testes ok.")
