#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 08/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5

def media(n):
    if type(n) != list:
        return Exception
    if len(n) == 0:
        return Exception
    for i in n:
        if type(i) != int:
            return Exception
    media = sum(n)/len(n)
    prox = n[0]
    menor = abs(prox - media)

    for i in n:
        dife = abs(i - media)
        if dife < menor:
            menor = dife
            prox = i
    return prox
    
assert media([-2, -5, -4, -6, -7]) == -5
assert media([4, 5, 6, 7, 8, 9]) == 6
assert media([12, 25, 24, 35]) == 24
assert media([1, 2, 3, 4, 5]) == 3
assert media([-1, -2, -3, -4, -5]) == -3

assert media([]) == Exception
assert media(["o", 2, 3, 4]) == Exception
assert media([True, False, 2, 3, 4]) == Exception
assert media([2.3, 2.3, 23, 4, 5, 6]) == Exception
assert media([None]) == Exception

print("Todos os testes ok.")
